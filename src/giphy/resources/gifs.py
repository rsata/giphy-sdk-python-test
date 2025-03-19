# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    gif_list_params,
    gif_search_params,
    gif_translate_params,
    gif_get_random_params,
    gif_get_trending_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.gif_list_response import GifListResponse
from ..types.gif_search_response import GifSearchResponse
from ..types.gif_retrieve_response import GifRetrieveResponse
from ..types.gif_translate_response import GifTranslateResponse
from ..types.gif_get_random_response import GifGetRandomResponse
from ..types.gif_get_trending_response import GifGetTrendingResponse

__all__ = ["GifsResource", "AsyncGifsResource"]


class GifsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GifsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/giphy-python#accessing-raw-response-data-eg-headers
        """
        return GifsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GifsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/giphy-python#with_streaming_response
        """
        return GifsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        gif_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GifRetrieveResponse:
        """
        Returns a GIF given that GIF's unique ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/gifs/{gif_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GifRetrieveResponse,
        )

    def list(
        self,
        *,
        ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GifListResponse:
        """
        A multiget version of the get GIF by ID endpoint.

        Args:
          ids: Filters results by specified GIF IDs, separated by commas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/gifs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ids": ids}, gif_list_params.GifListParams),
            ),
            cast_to=GifListResponse,
        )

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
    ) -> GifGetRandomResponse:
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
            "/gifs/random",
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
                    gif_get_random_params.GifGetRandomParams,
                ),
            ),
            cast_to=GifGetRandomResponse,
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
    ) -> GifGetTrendingResponse:
        """Fetch GIFs currently trending online.

        Hand curated by the GIPHY editorial team.
        The data returned mirrors the GIFs showcased on the GIPHY homepage. Returns 25
        results by default.

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
            "/gifs/trending",
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
                    gif_get_trending_params.GifGetTrendingParams,
                ),
            ),
            cast_to=GifGetTrendingResponse,
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
    ) -> GifSearchResponse:
        """Search all GIPHY GIFs for a word or phrase.

        Punctuation will be stripped and
        ignored. Use a plus or url encode for phrases. Example paul+rudd, ryan+gosling
        or american+psycho.

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
            "/gifs/search",
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
                    gif_search_params.GifSearchParams,
                ),
            ),
            cast_to=GifSearchResponse,
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
    ) -> GifTranslateResponse:
        """
        The translate API draws on search, but uses the GIPHY `special sauce` to handle
        translating from one vocabulary to another. In this case, words and phrases to
        GIF

        Args:
          s: Search term.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/gifs/translate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"s": s}, gif_translate_params.GifTranslateParams),
            ),
            cast_to=GifTranslateResponse,
        )


class AsyncGifsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGifsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/giphy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGifsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGifsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/giphy-python#with_streaming_response
        """
        return AsyncGifsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        gif_id: int,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GifRetrieveResponse:
        """
        Returns a GIF given that GIF's unique ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/gifs/{gif_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GifRetrieveResponse,
        )

    async def list(
        self,
        *,
        ids: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GifListResponse:
        """
        A multiget version of the get GIF by ID endpoint.

        Args:
          ids: Filters results by specified GIF IDs, separated by commas.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/gifs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ids": ids}, gif_list_params.GifListParams),
            ),
            cast_to=GifListResponse,
        )

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
    ) -> GifGetRandomResponse:
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
            "/gifs/random",
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
                    gif_get_random_params.GifGetRandomParams,
                ),
            ),
            cast_to=GifGetRandomResponse,
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
    ) -> GifGetTrendingResponse:
        """Fetch GIFs currently trending online.

        Hand curated by the GIPHY editorial team.
        The data returned mirrors the GIFs showcased on the GIPHY homepage. Returns 25
        results by default.

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
            "/gifs/trending",
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
                    gif_get_trending_params.GifGetTrendingParams,
                ),
            ),
            cast_to=GifGetTrendingResponse,
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
    ) -> GifSearchResponse:
        """Search all GIPHY GIFs for a word or phrase.

        Punctuation will be stripped and
        ignored. Use a plus or url encode for phrases. Example paul+rudd, ryan+gosling
        or american+psycho.

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
            "/gifs/search",
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
                    gif_search_params.GifSearchParams,
                ),
            ),
            cast_to=GifSearchResponse,
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
    ) -> GifTranslateResponse:
        """
        The translate API draws on search, but uses the GIPHY `special sauce` to handle
        translating from one vocabulary to another. In this case, words and phrases to
        GIF

        Args:
          s: Search term.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/gifs/translate",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"s": s}, gif_translate_params.GifTranslateParams),
            ),
            cast_to=GifTranslateResponse,
        )


class GifsResourceWithRawResponse:
    def __init__(self, gifs: GifsResource) -> None:
        self._gifs = gifs

        self.retrieve = to_raw_response_wrapper(
            gifs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            gifs.list,
        )
        self.get_random = to_raw_response_wrapper(
            gifs.get_random,
        )
        self.get_trending = to_raw_response_wrapper(
            gifs.get_trending,
        )
        self.search = to_raw_response_wrapper(
            gifs.search,
        )
        self.translate = to_raw_response_wrapper(
            gifs.translate,
        )


class AsyncGifsResourceWithRawResponse:
    def __init__(self, gifs: AsyncGifsResource) -> None:
        self._gifs = gifs

        self.retrieve = async_to_raw_response_wrapper(
            gifs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            gifs.list,
        )
        self.get_random = async_to_raw_response_wrapper(
            gifs.get_random,
        )
        self.get_trending = async_to_raw_response_wrapper(
            gifs.get_trending,
        )
        self.search = async_to_raw_response_wrapper(
            gifs.search,
        )
        self.translate = async_to_raw_response_wrapper(
            gifs.translate,
        )


class GifsResourceWithStreamingResponse:
    def __init__(self, gifs: GifsResource) -> None:
        self._gifs = gifs

        self.retrieve = to_streamed_response_wrapper(
            gifs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            gifs.list,
        )
        self.get_random = to_streamed_response_wrapper(
            gifs.get_random,
        )
        self.get_trending = to_streamed_response_wrapper(
            gifs.get_trending,
        )
        self.search = to_streamed_response_wrapper(
            gifs.search,
        )
        self.translate = to_streamed_response_wrapper(
            gifs.translate,
        )


class AsyncGifsResourceWithStreamingResponse:
    def __init__(self, gifs: AsyncGifsResource) -> None:
        self._gifs = gifs

        self.retrieve = async_to_streamed_response_wrapper(
            gifs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            gifs.list,
        )
        self.get_random = async_to_streamed_response_wrapper(
            gifs.get_random,
        )
        self.get_trending = async_to_streamed_response_wrapper(
            gifs.get_trending,
        )
        self.search = async_to_streamed_response_wrapper(
            gifs.search,
        )
        self.translate = async_to_streamed_response_wrapper(
            gifs.translate,
        )
