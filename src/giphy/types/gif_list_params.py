# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GifListParams"]


class GifListParams(TypedDict, total=False):
    ids: str
    """Filters results by specified GIF IDs, separated by commas."""
