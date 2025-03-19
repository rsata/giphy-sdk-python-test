# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Image"]


class Image(BaseModel):
    frames: Optional[str] = None
    """The number of frames in this GIF."""

    height: Optional[str] = None
    """The height of this GIF in pixels."""

    mp4: Optional[str] = None
    """The URL for this GIF in .MP4 format."""

    mp4_size: Optional[str] = None
    """The size in bytes of the .MP4 file corresponding to this GIF."""

    size: Optional[str] = None
    """The size of this GIF in bytes."""

    url: Optional[str] = None
    """The publicly-accessible direct URL for this GIF."""

    webp: Optional[str] = None
    """The URL for this GIF in .webp format."""

    webp_size: Optional[str] = None
    """The size in bytes of the .webp file corresponding to this GIF."""

    width: Optional[str] = None
    """The width of this GIF in pixels."""
