#!/usr/bin/env python3

"""
Example of using DeepSDF to compute SDFs for arbitrary meshes, and the Rerun SDK to visualize the
results. log the Objectron dataset.

@InProceedings{Park_2019_CVPR,
    author = {
        Park,
        Jeong Joon and Florence,
        Peter and Straub,
        Julian and Newcombe,
        Richard and Lovegrove,
        Steven,
    },
    title = {DeepSDF: Learning Continuous Signed Distance Functions for Shape Representation},
    booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
    month = {June},
    year = {2019}
}

Setup:
```sh
(cd examples/deep_sdf && ./download_dataset.py)
```

Run:
```sh
# assuming your virtual env is up
python3 examples/deep_sdf/main.py examples/deep_sdf/dataset/buddha/buddha.obj
```
"""


import argparse
import sys

import mesh_to_sdf
import numpy as np
import rerun_sdk as rerun
import trimesh

from pathlib import Path
from typing import Tuple, cast

from scipy.spatial.transform import Rotation as R
from trimesh import Trimesh


def read_mesh(path: Path) -> Trimesh:
    print(f"loading mesh {path}...")
    mesh = trimesh.load(path)
    return cast(Trimesh, mesh)


def compute_voxel_sdf(mesh: Trimesh) -> np.ndarray:
    voxvol = mesh_to_sdf.mesh_to_voxels(mesh, voxel_resolution=64)
    return voxvol


def compute_sample_sdf(mesh: Trimesh) -> Tuple[np.ndarray, np.ndarray]:
    points, sdf, _ = mesh_to_sdf.sample_sdf_near_surface(mesh,
                                                         number_of_points=250000,
                                                         return_gradients=True)
    return (points, sdf)


def log_mesh(path: Path, mesh: Trimesh, points: np.ndarray, sdf: np.ndarray):
    rerun.log_points("sdf/inside",
                     points[sdf <= 0],
                     colors=np.array([255, 0, 0, 255]),
                     space="world")
    rerun.log_points("sdf/outside",
                     points[sdf > 0],
                     colors=np.array([0, 255, 0, 255]),
                     space="world")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Generates SDFs for arbitrary meshes and logs the results using the Rerun SDK.')
    parser.add_argument('--headless', action='store_true',
                        help="Don't show GUI")
    parser.add_argument('--connect', dest='connect', action='store_true',
                        help='Connect to an external viewer')
    parser.add_argument('--addr', type=str, default=None,
                        help='Connect to this ip:port')
    parser.add_argument('--save', type=str, default=None,
                        help='Save data to a .rrd file at this path')
    parser.add_argument('--frames', type=int, default=sys.maxsize,
                        help='If specifies, limits the number of frames logged')
    parser.add_argument('path', type=Path, nargs='+',
                        help='Mesh(es) to log (e.g. `dataset/buddha/buddha.obj`)')
    args = parser.parse_args()

    if args.connect:
        # Send logging data to separate `rerun` process.
        # You can ommit the argument to connect to the default address,
        # which is `127.0.0.1:9876`.
        rerun.connect(args.addr)

    for path in args.path:
        # TODO(cmc): gotta fix .obj loading on the Rust side first :(
        # with open(path, mode='rb') as file:
        #     rerun.log_mesh_file("mesh", MeshFormat.OBJ, file.read())
        mesh = read_mesh(path)
        (points, sdf) = compute_sample_sdf(mesh)
        voxvol = compute_voxel_sdf(mesh)
        log_mesh(path, mesh, points, sdf)
        rerun.log_image("sdf/slice/#10", voxvol[10])
        rerun.log_image("sdf/slice/#30", voxvol[30])
        rerun.log_image("sdf/slice/#50", voxvol[50])

    if args.save is not None:
        rerun.save(args.save)
    elif args.headless:
        pass
    elif not args.connect:
        rerun.show()
