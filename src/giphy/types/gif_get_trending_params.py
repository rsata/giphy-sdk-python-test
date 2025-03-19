# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GifGetTrendingParams"]


class GifGetTrendingParams(TypedDict, total=False):
    limit: int
    """The maximum number of records to return."""

    offset: int
    """An optional results offset."""

    rating: str
    """Filters results by specified rating."""
