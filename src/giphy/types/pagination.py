# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Pagination"]


class Pagination(BaseModel):
    count: Optional[int] = None
    """Total number of items returned."""

    offset: Optional[int] = None
    """Position in pagination."""

    total_count: Optional[int] = None
    """Total number of items available."""
