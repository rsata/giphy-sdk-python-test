# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GiffffGetRandomParams"]


class GiffffGetRandomParams(TypedDict, total=False):
    rating: str
    """Filters results by specified rating."""

    tag: str
    """Filters results by specified tag."""
