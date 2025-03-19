# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giphy import Giphy, AsyncGiphy
from giphy.types import (
    GifListResponse,
    GifSearchResponse,
    GifRetrieveResponse,
    GifGetRandomResponse,
    GifTranslateResponse,
    GifGetTrendingResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGifs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Giphy) -> None:
        gif = client.gifs.retrieve(
            0,
        )
        assert_matches_type(GifRetrieveResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Giphy) -> None:
        response = client.gifs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = response.parse()
        assert_matches_type(GifRetrieveResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Giphy) -> None:
        with client.gifs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = response.parse()
            assert_matches_type(GifRetrieveResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Giphy) -> None:
        gif = client.gifs.list()
        assert_matches_type(GifListResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Giphy) -> None:
        gif = client.gifs.list(
            ids="ids",
        )
        assert_matches_type(GifListResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Giphy) -> None:
        response = client.gifs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = response.parse()
        assert_matches_type(GifListResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Giphy) -> None:
        with client.gifs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = response.parse()
            assert_matches_type(GifListResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_random(self, client: Giphy) -> None:
        gif = client.gifs.get_random()
        assert_matches_type(GifGetRandomResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_random_with_all_params(self, client: Giphy) -> None:
        gif = client.gifs.get_random(
            rating="rating",
            tag="tag",
        )
        assert_matches_type(GifGetRandomResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_random(self, client: Giphy) -> None:
        response = client.gifs.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = response.parse()
        assert_matches_type(GifGetRandomResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_random(self, client: Giphy) -> None:
        with client.gifs.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = response.parse()
            assert_matches_type(GifGetRandomResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_trending(self, client: Giphy) -> None:
        gif = client.gifs.get_trending()
        assert_matches_type(GifGetTrendingResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_trending_with_all_params(self, client: Giphy) -> None:
        gif = client.gifs.get_trending(
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(GifGetTrendingResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_trending(self, client: Giphy) -> None:
        response = client.gifs.with_raw_response.get_trending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = response.parse()
        assert_matches_type(GifGetTrendingResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_trending(self, client: Giphy) -> None:
        with client.gifs.with_streaming_response.get_trending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = response.parse()
            assert_matches_type(GifGetTrendingResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: Giphy) -> None:
        gif = client.gifs.search(
            q="q",
        )
        assert_matches_type(GifSearchResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_with_all_params(self, client: Giphy) -> None:
        gif = client.gifs.search(
            q="q",
            lang="lang",
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(GifSearchResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: Giphy) -> None:
        response = client.gifs.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = response.parse()
        assert_matches_type(GifSearchResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: Giphy) -> None:
        with client.gifs.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = response.parse()
            assert_matches_type(GifSearchResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_translate(self, client: Giphy) -> None:
        gif = client.gifs.translate(
            s="s",
        )
        assert_matches_type(GifTranslateResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_translate(self, client: Giphy) -> None:
        response = client.gifs.with_raw_response.translate(
            s="s",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = response.parse()
        assert_matches_type(GifTranslateResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_translate(self, client: Giphy) -> None:
        with client.gifs.with_streaming_response.translate(
            s="s",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = response.parse()
            assert_matches_type(GifTranslateResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGifs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.retrieve(
            0,
        )
        assert_matches_type(GifRetrieveResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGiphy) -> None:
        response = await async_client.gifs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = await response.parse()
        assert_matches_type(GifRetrieveResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGiphy) -> None:
        async with async_client.gifs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = await response.parse()
            assert_matches_type(GifRetrieveResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.list()
        assert_matches_type(GifListResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.list(
            ids="ids",
        )
        assert_matches_type(GifListResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGiphy) -> None:
        response = await async_client.gifs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = await response.parse()
        assert_matches_type(GifListResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGiphy) -> None:
        async with async_client.gifs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = await response.parse()
            assert_matches_type(GifListResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_random(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.get_random()
        assert_matches_type(GifGetRandomResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_random_with_all_params(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.get_random(
            rating="rating",
            tag="tag",
        )
        assert_matches_type(GifGetRandomResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_random(self, async_client: AsyncGiphy) -> None:
        response = await async_client.gifs.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = await response.parse()
        assert_matches_type(GifGetRandomResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_random(self, async_client: AsyncGiphy) -> None:
        async with async_client.gifs.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = await response.parse()
            assert_matches_type(GifGetRandomResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_trending(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.get_trending()
        assert_matches_type(GifGetTrendingResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_trending_with_all_params(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.get_trending(
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(GifGetTrendingResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_trending(self, async_client: AsyncGiphy) -> None:
        response = await async_client.gifs.with_raw_response.get_trending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = await response.parse()
        assert_matches_type(GifGetTrendingResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_trending(self, async_client: AsyncGiphy) -> None:
        async with async_client.gifs.with_streaming_response.get_trending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = await response.parse()
            assert_matches_type(GifGetTrendingResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.search(
            q="q",
        )
        assert_matches_type(GifSearchResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.search(
            q="q",
            lang="lang",
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(GifSearchResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncGiphy) -> None:
        response = await async_client.gifs.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = await response.parse()
        assert_matches_type(GifSearchResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncGiphy) -> None:
        async with async_client.gifs.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = await response.parse()
            assert_matches_type(GifSearchResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_translate(self, async_client: AsyncGiphy) -> None:
        gif = await async_client.gifs.translate(
            s="s",
        )
        assert_matches_type(GifTranslateResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_translate(self, async_client: AsyncGiphy) -> None:
        response = await async_client.gifs.with_raw_response.translate(
            s="s",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        gif = await response.parse()
        assert_matches_type(GifTranslateResponse, gif, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_translate(self, async_client: AsyncGiphy) -> None:
        async with async_client.gifs.with_streaming_response.translate(
            s="s",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            gif = await response.parse()
            assert_matches_type(GifTranslateResponse, gif, path=["response"])

        assert cast(Any, response.is_closed) is True
