# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    giffff_list_params,
    giffff_search_params,
    giffff_translate_params,
    giffff_get_random_params,
    giffff_get_trending_params,
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
from ..types.giffff_list_response import GiffffListResponse
from ..types.giffff_search_response import GiffffSearchResponse
from ..types.giffff_retrieve_response import GiffffRetrieveResponse
from ..types.giffff_translate_response import GiffffTranslateResponse
from ..types.giffff_get_random_response import GiffffGetRandomResponse
from ..types.giffff_get_trending_response import GiffffGetTrendingResponse

__all__ = ["GiffffsResource", "AsyncGiffffsResource"]


class GiffffsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GiffffsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsata/giphy-sdk-python-test#accessing-raw-response-data-eg-headers
        """
        return GiffffsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GiffffsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsata/giphy-sdk-python-test#with_streaming_response
        """
        return GiffffsResourceWithStreamingResponse(self)

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
    ) -> GiffffRetrieveResponse:
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
            cast_to=GiffffRetrieveResponse,
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
    ) -> GiffffListResponse:
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
                query=maybe_transform({"ids": ids}, giffff_list_params.GiffffListParams),
            ),
            cast_to=GiffffListResponse,
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
    ) -> GiffffGetRandomResponse:
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
                    giffff_get_random_params.GiffffGetRandomParams,
                ),
            ),
            cast_to=GiffffGetRandomResponse,
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
    ) -> GiffffGetTrendingResponse:
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
                    giffff_get_trending_params.GiffffGetTrendingParams,
                ),
            ),
            cast_to=GiffffGetTrendingResponse,
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
    ) -> GiffffSearchResponse:
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
                    giffff_search_params.GiffffSearchParams,
                ),
            ),
            cast_to=GiffffSearchResponse,
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
    ) -> GiffffTranslateResponse:
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
                query=maybe_transform({"s": s}, giffff_translate_params.GiffffTranslateParams),
            ),
            cast_to=GiffffTranslateResponse,
        )


class AsyncGiffffsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGiffffsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/rsata/giphy-sdk-python-test#accessing-raw-response-data-eg-headers
        """
        return AsyncGiffffsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGiffffsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/rsata/giphy-sdk-python-test#with_streaming_response
        """
        return AsyncGiffffsResourceWithStreamingResponse(self)

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
    ) -> GiffffRetrieveResponse:
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
            cast_to=GiffffRetrieveResponse,
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
    ) -> GiffffListResponse:
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
                query=await async_maybe_transform({"ids": ids}, giffff_list_params.GiffffListParams),
            ),
            cast_to=GiffffListResponse,
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
    ) -> GiffffGetRandomResponse:
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
                    giffff_get_random_params.GiffffGetRandomParams,
                ),
            ),
            cast_to=GiffffGetRandomResponse,
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
    ) -> GiffffGetTrendingResponse:
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
                    giffff_get_trending_params.GiffffGetTrendingParams,
                ),
            ),
            cast_to=GiffffGetTrendingResponse,
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
    ) -> GiffffSearchResponse:
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
                    giffff_search_params.GiffffSearchParams,
                ),
            ),
            cast_to=GiffffSearchResponse,
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
    ) -> GiffffTranslateResponse:
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
                query=await async_maybe_transform({"s": s}, giffff_translate_params.GiffffTranslateParams),
            ),
            cast_to=GiffffTranslateResponse,
        )


class GiffffsResourceWithRawResponse:
    def __init__(self, giffffs: GiffffsResource) -> None:
        self._giffffs = giffffs

        self.retrieve = to_raw_response_wrapper(
            giffffs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            giffffs.list,
        )
        self.get_random = to_raw_response_wrapper(
            giffffs.get_random,
        )
        self.get_trending = to_raw_response_wrapper(
            giffffs.get_trending,
        )
        self.search = to_raw_response_wrapper(
            giffffs.search,
        )
        self.translate = to_raw_response_wrapper(
            giffffs.translate,
        )


class AsyncGiffffsResourceWithRawResponse:
    def __init__(self, giffffs: AsyncGiffffsResource) -> None:
        self._giffffs = giffffs

        self.retrieve = async_to_raw_response_wrapper(
            giffffs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            giffffs.list,
        )
        self.get_random = async_to_raw_response_wrapper(
            giffffs.get_random,
        )
        self.get_trending = async_to_raw_response_wrapper(
            giffffs.get_trending,
        )
        self.search = async_to_raw_response_wrapper(
            giffffs.search,
        )
        self.translate = async_to_raw_response_wrapper(
            giffffs.translate,
        )


class GiffffsResourceWithStreamingResponse:
    def __init__(self, giffffs: GiffffsResource) -> None:
        self._giffffs = giffffs

        self.retrieve = to_streamed_response_wrapper(
            giffffs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            giffffs.list,
        )
        self.get_random = to_streamed_response_wrapper(
            giffffs.get_random,
        )
        self.get_trending = to_streamed_response_wrapper(
            giffffs.get_trending,
        )
        self.search = to_streamed_response_wrapper(
            giffffs.search,
        )
        self.translate = to_streamed_response_wrapper(
            giffffs.translate,
        )


class AsyncGiffffsResourceWithStreamingResponse:
    def __init__(self, giffffs: AsyncGiffffsResource) -> None:
        self._giffffs = giffffs

        self.retrieve = async_to_streamed_response_wrapper(
            giffffs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            giffffs.list,
        )
        self.get_random = async_to_streamed_response_wrapper(
            giffffs.get_random,
        )
        self.get_trending = async_to_streamed_response_wrapper(
            giffffs.get_trending,
        )
        self.search = async_to_streamed_response_wrapper(
            giffffs.search,
        )
        self.translate = async_to_streamed_response_wrapper(
            giffffs.translate,
        )
