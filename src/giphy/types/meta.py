# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Meta"]


class Meta(BaseModel):
    msg: Optional[str] = None
    """HTTP Response Message"""

    response_id: Optional[str] = None
    """A unique ID paired with this response from the API."""

    status: Optional[int] = None
    """HTTP Response Code"""
