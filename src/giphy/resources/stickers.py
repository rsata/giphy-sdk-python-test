# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    sticker_search_params,
    sticker_translate_params,
    sticker_get_random_params,
    sticker_get_trending_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.sticker_search_response import StickerSearchResponse
from ..types.sticker_translate_response import StickerTranslateResponse
from ..types.sticker_get_random_response import StickerGetRandomResponse
from ..types.sticker_get_trending_response import StickerGetTrendingResponse

__all__ = ["StickersResource", "AsyncStickersResource"]


class StickersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StickersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsata/giphy-sdk-python-test#accessing-raw-response-data-eg-headers
        """
        return StickersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StickersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsata/giphy-sdk-python-test#with_streaming_response
        """
        return StickersResourceWithStreamingResponse(self)

    def get_random(
        self,
        *,
        rating: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StickerGetRandomResponse:
        """Returns a random GIF, limited by tag.

        Excluding the tag parameter will return a
        random GIF from the GIPHY catalog.

        Args:
          rating: Filters results by specified rating.

          tag: Filters results by specified tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stickers/random",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "rating": rating,
                        "tag": tag,
                    },
                    sticker_get_random_params.StickerGetRandomParams,
                ),
            ),
            cast_to=StickerGetRandomResponse,
        )

    def get_trending(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        rating: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StickerGetTrendingResponse:
        """Fetch Stickers currently trending online.

        Hand curated by the GIPHY editorial
        team. Returns 25 results by default.

        Args:
          limit: The maximum number of records to return.

          offset: An optional results offset.

          rating: Filters results by specified rating.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stickers/trending",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "rating": rating,
                    },
                    sticker_get_trending_params.StickerGetTrendingParams,
                ),
            ),
            cast_to=StickerGetTrendingResponse,
        )

    def search(
        self,
        *,
        q: str,
        lang: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        rating: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StickerSearchResponse:
        """
        Replicates the functionality and requirements of the classic GIPHY search, but
        returns animated stickers rather than GIFs.

        Args:
          q: Search query term or prhase.

          lang: Specify default language for regional content; use a 2-letter ISO 639-1 language
              code.

          limit: The maximum number of records to return.

          offset: An optional results offset.

          rating: Filters results by specified rating.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stickers/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "q": q,
                        "lang": lang,
                        "limit": limit,
                        "offset": offset,
                        "rating": rating,
                    },
                    sticker_search_params.StickerSearchParams,
                ),
            ),
            cast_to=StickerSearchResponse,
        )

    def translate(
        self,
        *,
        s: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StickerTranslateResponse:
        """
        The translate API draws on search, but uses the GIPHY `special sauce` to handle
        translating from one vocabulary to another. In this case, words and phrases to
        GIFs.

        Args:
          s: Search term.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/stickers/translate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"s": s}, sticker_translate_params.StickerTranslateParams),
            ),
            cast_to=StickerTranslateResponse,
        )


class AsyncStickersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStickersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsata/giphy-sdk-python-test#accessing-raw-response-data-eg-headers
        """
        return AsyncStickersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStickersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsata/giphy-sdk-python-test#with_streaming_response
        """
        return AsyncStickersResourceWithStreamingResponse(self)

    async def get_random(
        self,
        *,
        rating: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StickerGetRandomResponse:
        """Returns a random GIF, limited by tag.

        Excluding the tag parameter will return a
        random GIF from the GIPHY catalog.

        Args:
          rating: Filters results by specified rating.

          tag: Filters results by specified tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stickers/random",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "rating": rating,
                        "tag": tag,
                    },
                    sticker_get_random_params.StickerGetRandomParams,
                ),
            ),
            cast_to=StickerGetRandomResponse,
        )

    async def get_trending(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        rating: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StickerGetTrendingResponse:
        """Fetch Stickers currently trending online.

        Hand curated by the GIPHY editorial
        team. Returns 25 results by default.

        Args:
          limit: The maximum number of records to return.

          offset: An optional results offset.

          rating: Filters results by specified rating.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stickers/trending",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                        "rating": rating,
                    },
                    sticker_get_trending_params.StickerGetTrendingParams,
                ),
            ),
            cast_to=StickerGetTrendingResponse,
        )

    async def search(
        self,
        *,
        q: str,
        lang: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        rating: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StickerSearchResponse:
        """
        Replicates the functionality and requirements of the classic GIPHY search, but
        returns animated stickers rather than GIFs.

        Args:
          q: Search query term or prhase.

          lang: Specify default language for regional content; use a 2-letter ISO 639-1 language
              code.

          limit: The maximum number of records to return.

          offset: An optional results offset.

          rating: Filters results by specified rating.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stickers/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "q": q,
                        "lang": lang,
                        "limit": limit,
                        "offset": offset,
                        "rating": rating,
                    },
                    sticker_search_params.StickerSearchParams,
                ),
            ),
            cast_to=StickerSearchResponse,
        )

    async def translate(
        self,
        *,
        s: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StickerTranslateResponse:
        """
        The translate API draws on search, but uses the GIPHY `special sauce` to handle
        translating from one vocabulary to another. In this case, words and phrases to
        GIFs.

        Args:
          s: Search term.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/stickers/translate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"s": s}, sticker_translate_params.StickerTranslateParams),
            ),
            cast_to=StickerTranslateResponse,
        )


class StickersResourceWithRawResponse:
    def __init__(self, stickers: StickersResource) -> None:
        self._stickers = stickers

        self.get_random = to_raw_response_wrapper(
            stickers.get_random,
        )
        self.get_trending = to_raw_response_wrapper(
            stickers.get_trending,
        )
        self.search = to_raw_response_wrapper(
            stickers.search,
        )
        self.translate = to_raw_response_wrapper(
            stickers.translate,
        )


class AsyncStickersResourceWithRawResponse:
    def __init__(self, stickers: AsyncStickersResource) -> None:
        self._stickers = stickers

        self.get_random = async_to_raw_response_wrapper(
            stickers.get_random,
        )
        self.get_trending = async_to_raw_response_wrapper(
            stickers.get_trending,
        )
        self.search = async_to_raw_response_wrapper(
            stickers.search,
        )
        self.translate = async_to_raw_response_wrapper(
            stickers.translate,
        )


class StickersResourceWithStreamingResponse:
    def __init__(self, stickers: StickersResource) -> None:
        self._stickers = stickers

        self.get_random = to_streamed_response_wrapper(
            stickers.get_random,
        )
        self.get_trending = to_streamed_response_wrapper(
            stickers.get_trending,
        )
        self.search = to_streamed_response_wrapper(
            stickers.search,
        )
        self.translate = to_streamed_response_wrapper(
            stickers.translate,
        )


class AsyncStickersResourceWithStreamingResponse:
    def __init__(self, stickers: AsyncStickersResource) -> None:
        self._stickers = stickers

        self.get_random = async_to_streamed_response_wrapper(
            stickers.get_random,
        )
        self.get_trending = async_to_streamed_response_wrapper(
            stickers.get_trending,
        )
        self.search = async_to_streamed_response_wrapper(
            stickers.search,
        )
        self.translate = async_to_streamed_response_wrapper(
            stickers.translate,
        )
