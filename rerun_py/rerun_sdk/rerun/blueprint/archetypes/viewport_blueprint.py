# DO NOT EDIT! This file was auto-generated by crates/re_types_builder/src/codegen/python.rs
# Based on "crates/re_types/definitions/rerun/blueprint/archetypes/viewport_blueprint.fbs".

# You can extend this class by creating a "ViewportBlueprintExt" class in "viewport_blueprint_ext.py".

from __future__ import annotations

from typing import Any

from attrs import define, field

from ... import blueprint, datatypes
from ..._baseclasses import Archetype
from ...error_utils import catch_and_log_exceptions

__all__ = ["ViewportBlueprint"]


@define(str=False, repr=False, init=False)
class ViewportBlueprint(Archetype):
    """**Archetype**: The top-level description of the Viewport."""

    def __init__(
        self: Any,
        space_views: blueprint.components.IncludedSpaceViewsLike,
        *,
        layout: blueprint.components.ViewportLayoutLike | None = None,
        root_container: datatypes.UuidLike | None = None,
        maximized: datatypes.UuidLike | None = None,
        auto_layout: blueprint.components.AutoLayoutLike | None = None,
        auto_space_views: blueprint.components.AutoSpaceViewsLike | None = None,
    ):
        """
        Create a new instance of the ViewportBlueprint archetype.

        Parameters
        ----------
        space_views:
            All of the space-views that belong to the viewport.
        layout:
            The layout of the space-views
        root_container:
            The layout of the space-views
        maximized:
            Show one tab as maximized?
        auto_layout:
            Whether the viewport layout is determined automatically.

            Set to `false` the first time the user messes around with the viewport blueprint.
        auto_space_views:
            Whether or not space views should be created automatically.

        """

        # You can define your own __init__ function as a member of ViewportBlueprintExt in viewport_blueprint_ext.py
        with catch_and_log_exceptions(context=self.__class__.__name__):
            self.__attrs_init__(
                space_views=space_views,
                layout=layout,
                root_container=root_container,
                maximized=maximized,
                auto_layout=auto_layout,
                auto_space_views=auto_space_views,
            )
            return
        self.__attrs_clear__()

    def __attrs_clear__(self) -> None:
        """Convenience method for calling `__attrs_init__` with all `None`s."""
        self.__attrs_init__(
            space_views=None,  # type: ignore[arg-type]
            layout=None,  # type: ignore[arg-type]
            root_container=None,  # type: ignore[arg-type]
            maximized=None,  # type: ignore[arg-type]
            auto_layout=None,  # type: ignore[arg-type]
            auto_space_views=None,  # type: ignore[arg-type]
        )

    @classmethod
    def _clear(cls) -> ViewportBlueprint:
        """Produce an empty ViewportBlueprint, bypassing `__init__`."""
        inst = cls.__new__(cls)
        inst.__attrs_clear__()
        return inst

    space_views: blueprint.components.IncludedSpaceViewsBatch = field(
        metadata={"component": "required"},
        converter=blueprint.components.IncludedSpaceViewsBatch._required,  # type: ignore[misc]
    )
    # All of the space-views that belong to the viewport.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    layout: blueprint.components.ViewportLayoutBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.ViewportLayoutBatch._optional,  # type: ignore[misc]
    )
    # The layout of the space-views
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    root_container: blueprint.components.RootContainerBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.RootContainerBatch._optional,  # type: ignore[misc]
    )
    # The layout of the space-views
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    maximized: blueprint.components.SpaceViewMaximizedBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.SpaceViewMaximizedBatch._optional,  # type: ignore[misc]
    )
    # Show one tab as maximized?
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    auto_layout: blueprint.components.AutoLayoutBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.AutoLayoutBatch._optional,  # type: ignore[misc]
    )
    # Whether the viewport layout is determined automatically.
    #
    # Set to `false` the first time the user messes around with the viewport blueprint.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    auto_space_views: blueprint.components.AutoSpaceViewsBatch | None = field(
        metadata={"component": "optional"},
        default=None,
        converter=blueprint.components.AutoSpaceViewsBatch._optional,  # type: ignore[misc]
    )
    # Whether or not space views should be created automatically.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    __str__ = Archetype.__str__
    __repr__ = Archetype.__repr__
