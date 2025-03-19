# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .image import Image
from .._models import BaseModel

__all__ = ["Gif", "Images", "User"]


class Images(BaseModel):
    downsized: Optional[Image] = None
    """Data surrounding a version of this GIF downsized to be under 2mb."""

    downsized_large: Optional[Image] = None
    """Data surrounding a version of this GIF downsized to be under 8mb."""

    downsized_medium: Optional[Image] = None
    """Data surrounding a version of this GIF downsized to be under 5mb."""

    downsized_small: Optional[Image] = None
    """Data surrounding a version of this GIF downsized to be under 200kb."""

    downsized_still: Optional[Image] = None
    """Data surrounding a static preview image of the downsized version of this GIF."""

    fixed_height: Optional[Image] = None
    """Data surrounding versions of this GIF with a fixed height of 200 pixels.

    Good for mobile use.
    """

    fixed_height_downsampled: Optional[Image] = None
    """
    Data surrounding versions of this GIF with a fixed height of 200 pixels and the
    number of frames reduced to 6.
    """

    fixed_height_small: Optional[Image] = None
    """Data surrounding versions of this GIF with a fixed height of 100 pixels.

    Good for mobile keyboards.
    """

    fixed_height_small_still: Optional[Image] = None
    """Data surrounding a static image of this GIF with a fixed height of 100 pixels."""

    fixed_height_still: Optional[Image] = None
    """Data surrounding a static image of this GIF with a fixed height of 200 pixels."""

    fixed_width: Optional[Image] = None
    """Data surrounding versions of this GIF with a fixed width of 200 pixels.

    Good for mobile use.
    """

    fixed_width_downsampled: Optional[Image] = None
    """
    Data surrounding versions of this GIF with a fixed width of 200 pixels and the
    number of frames reduced to 6.
    """

    fixed_width_small: Optional[Image] = None
    """Data surrounding versions of this GIF with a fixed width of 100 pixels.

    Good for mobile keyboards.
    """

    fixed_width_small_still: Optional[Image] = None
    """Data surrounding a static image of this GIF with a fixed width of 100 pixels."""

    fixed_width_still: Optional[Image] = None
    """Data surrounding a static image of this GIF with a fixed width of 200 pixels."""

    looping: Optional[Image] = None
    """Data surrounding a version of this GIF set to loop for 15 seconds."""

    original: Optional[Image] = None
    """Data surrounding the original version of this GIF. Good for desktop use."""

    original_still: Optional[Image] = None
    """Data surrounding a static preview image of the original GIF."""

    preview: Optional[Image] = None
    """
    Data surrounding a version of this GIF in .MP4 format limited to 50kb that
    displays the first 1-2 seconds of the GIF.
    """

    preview_gif: Optional[Image] = None
    """
    Data surrounding a version of this GIF limited to 50kb that displays the first
    1-2 seconds of the GIF.
    """


class User(BaseModel):
    avatar_url: Optional[str] = None
    """The URL for this user's avatar image."""

    banner_url: Optional[str] = None
    """The URL for the banner image that appears atop this user's profile page."""

    display_name: Optional[str] = None
    """
    The display name associated with this user (contains formatting the base
    username might not).
    """

    profile_url: Optional[str] = None
    """The URL for this user's profile."""

    twitter: Optional[str] = None
    """The Twitter username associated with this user, if applicable."""

    username: Optional[str] = None
    """The username associated with this user."""


class Gif(BaseModel):
    id: Optional[str] = None
    """This GIF's unique ID"""

    bitly_url: Optional[str] = None
    """The unique bit.ly URL for this GIF"""

    content_url: Optional[str] = None
    """Currently unused"""

    create_datetime: Optional[datetime] = None
    """The date this GIF was added to the GIPHY database."""

    embded_url: Optional[str] = None
    """A URL used for embedding this GIF"""

    featured_tags: Optional[List[str]] = None
    """
    An array of featured tags for this GIF (Note: Not available when using the
    Public Beta Key)
    """

    images: Optional[Images] = None
    """An object containing data for various available formats and sizes of this GIF."""

    import_datetime: Optional[datetime] = None
    """The creation or upload date from this GIF's source."""

    rating: Optional[str] = None
    """The MPAA-style rating for this content. Examples include Y, G, PG, PG-13 and R"""

    slug: Optional[str] = None
    """The unique slug used in this GIF's URL"""

    source: Optional[str] = None
    """The page on which this GIF was found"""

    source_post_url: Optional[str] = None
    """The URL of the webpage on which this GIF was found."""

    source_tld: Optional[str] = None
    """The top level domain of the source URL."""

    tags: Optional[List[str]] = None
    """
    An array of tags for this GIF (Note: Not available when using the Public Beta
    Key)
    """

    trending_datetime: Optional[datetime] = None
    """The date on which this gif was marked trending, if applicable."""

    type: Optional[Literal["gif"]] = None
    """Type of the gif. By default, this is almost always gif"""

    update_datetime: Optional[datetime] = None
    """The date on which this GIF was last updated."""

    url: Optional[str] = None
    """The unique URL for this GIF"""

    user: Optional[User] = None
    """
    The User Object contains information about the user associated with a GIF and
    URLs to assets such as that user's avatar image, profile, and more.
    """

    username: Optional[str] = None
    """The username this GIF is attached to, if applicable"""
