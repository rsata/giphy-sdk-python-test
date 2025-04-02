# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .gif import Gif
from .meta import Meta
from .._models import BaseModel
from .pagination import Pagination

__all__ = ["GiffffGetTrendingResponse"]


class GiffffGetTrendingResponse(BaseModel):
    data: Optional[List[Gif]] = None

    meta: Optional[Meta] = None
    """
    The Meta Object contains basic information regarding the request, whether it was
    successful, and the response given by the API. Check `responses` to see a
    description of types of response codes the API might give you under different
    cirumstances.
    """

    pagination: Optional[Pagination] = None
    """
    The Pagination Object contains information relating to the number of total
    results available as well as the number of results fetched and their relative
    positions.
    """
