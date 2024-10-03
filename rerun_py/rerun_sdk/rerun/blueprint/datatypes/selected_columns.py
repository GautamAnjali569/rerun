# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/blueprint/datatypes/selected_columns.fbs".

# You can extend this class by creating a "SelectedColumnsExt" class in "selected_columns_ext.py".

from __future__ import annotations

from typing import Any, Sequence, Union

import pyarrow as pa
from attrs import define, field

from ... import datatypes
from ..._baseclasses import (
    BaseBatch,
    BaseExtensionType,
)
from ...blueprint import datatypes as blueprint_datatypes

__all__ = [
    "SelectedColumns",
    "SelectedColumnsArrayLike",
    "SelectedColumnsBatch",
    "SelectedColumnsLike",
    "SelectedColumnsType",
]


@define(init=False)
class SelectedColumns:
    """**Datatype**: List of selected columns in a dataframe."""

    def __init__(
        self: Any,
        time_columns: datatypes.Utf8ArrayLike,
        component_columns: blueprint_datatypes.ComponentColumnSelectorArrayLike,
    ):
        """
        Create a new instance of the SelectedColumns datatype.

        Parameters
        ----------
        time_columns:
            The time columns to include
        component_columns:
            The component columns to include

        """

        # You can define your own __init__ function as a member of SelectedColumnsExt in selected_columns_ext.py
        self.__attrs_init__(time_columns=time_columns, component_columns=component_columns)

    time_columns: list[datatypes.Utf8] = field()
    # The time columns to include
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    component_columns: list[blueprint_datatypes.ComponentColumnSelector] = field()
    # The component columns to include
    #
    # (Docstring intentionally commented out to hide this field from the docs)


SelectedColumnsLike = SelectedColumns
SelectedColumnsArrayLike = Union[
    SelectedColumns,
    Sequence[SelectedColumnsLike],
]


class SelectedColumnsType(BaseExtensionType):
    _TYPE_NAME: str = "rerun.blueprint.datatypes.SelectedColumns"

    def __init__(self) -> None:
        pa.ExtensionType.__init__(
            self,
            pa.struct([
                pa.field(
                    "time_columns",
                    pa.list_(pa.field("item", pa.utf8(), nullable=False, metadata={})),
                    nullable=False,
                    metadata={},
                ),
                pa.field(
                    "component_columns",
                    pa.list_(
                        pa.field(
                            "item",
                            pa.struct([
                                pa.field("entity_path", pa.utf8(), nullable=False, metadata={}),
                                pa.field("component", pa.utf8(), nullable=False, metadata={}),
                            ]),
                            nullable=False,
                            metadata={},
                        )
                    ),
                    nullable=False,
                    metadata={},
                ),
            ]),
            self._TYPE_NAME,
        )


class SelectedColumnsBatch(BaseBatch[SelectedColumnsArrayLike]):
    _ARROW_TYPE = SelectedColumnsType()

    @staticmethod
    def _native_to_pa_array(data: SelectedColumnsArrayLike, data_type: pa.DataType) -> pa.Array:
        raise NotImplementedError(
            "Arrow serialization of SelectedColumns not implemented: We lack codegen for arrow-serialization of general structs"
        )  # You need to implement native_to_pa_array_override in selected_columns_ext.py