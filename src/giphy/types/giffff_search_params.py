# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["GiffffSearchParams"]


class GiffffSearchParams(TypedDict, total=False):
    q: Required[str]
    """Search query term or prhase."""

    lang: str
    """
    Specify default language for regional content; use a 2-letter ISO 639-1 language
    code.
    """

    limit: int
    """The maximum number of records to return."""

    offset: int
    """An optional results offset."""

    rating: str
    """Filters results by specified rating."""
