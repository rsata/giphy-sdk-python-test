# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .gif import Gif
from .meta import Meta
from .._models import BaseModel

__all__ = ["GiffffTranslateResponse"]


class GiffffTranslateResponse(BaseModel):
    data: Optional[Gif] = None

    meta: Optional[Meta] = None
    """
    The Meta Object contains basic information regarding the request, whether it was
    successful, and the response given by the API. Check `responses` to see a
    description of types of response codes the API might give you under different
    cirumstances.
    """
