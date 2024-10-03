# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/blueprint/components/filter_by_range.fbs".

# You can extend this class by creating a "FilterByRangeExt" class in "filter_by_range_ext.py".

from __future__ import annotations

from ..._baseclasses import (
    ComponentBatchMixin,
    ComponentMixin,
)
from ...blueprint import datatypes as blueprint_datatypes

__all__ = ["FilterByRange", "FilterByRangeBatch", "FilterByRangeType"]


class FilterByRange(blueprint_datatypes.FilterByRange, ComponentMixin):
    """**Component**: Configuration for a filter-by-range feature of the dataframe view."""

    _BATCH_TYPE = None
    # You can define your own __init__ function as a member of FilterByRangeExt in filter_by_range_ext.py

    # Note: there are no fields here because FilterByRange delegates to datatypes.FilterByRange
    pass


class FilterByRangeType(blueprint_datatypes.FilterByRangeType):
    _TYPE_NAME: str = "rerun.blueprint.components.FilterByRange"


class FilterByRangeBatch(blueprint_datatypes.FilterByRangeBatch, ComponentBatchMixin):
    _ARROW_TYPE = FilterByRangeType()


# This is patched in late to avoid circular dependencies.
FilterByRange._BATCH_TYPE = FilterByRangeBatch  # type: ignore[assignment]