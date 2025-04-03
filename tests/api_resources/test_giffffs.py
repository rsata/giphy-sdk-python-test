# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giphy import Giphy2, AsyncGiphy2
from giphy.types import (
    GiffffListResponse,
    GiffffSearchResponse,
    GiffffRetrieveResponse,
    GiffffGetRandomResponse,
    GiffffTranslateResponse,
    GiffffGetTrendingResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGiffffs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve(self, client: Giphy2) -> None:
        giffff = client.giffffs.retrieve(
            0,
        )
        assert_matches_type(GiffffRetrieveResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve(self, client: Giphy2) -> None:
        response = client.giffffs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = response.parse()
        assert_matches_type(GiffffRetrieveResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve(self, client: Giphy2) -> None:
        with client.giffffs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = response.parse()
            assert_matches_type(GiffffRetrieveResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Giphy2) -> None:
        giffff = client.giffffs.list()
        assert_matches_type(GiffffListResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Giphy2) -> None:
        giffff = client.giffffs.list(
            ids="ids",
        )
        assert_matches_type(GiffffListResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Giphy2) -> None:
        response = client.giffffs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = response.parse()
        assert_matches_type(GiffffListResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Giphy2) -> None:
        with client.giffffs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = response.parse()
            assert_matches_type(GiffffListResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_random(self, client: Giphy2) -> None:
        giffff = client.giffffs.get_random()
        assert_matches_type(GiffffGetRandomResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_random_with_all_params(self, client: Giphy2) -> None:
        giffff = client.giffffs.get_random(
            rating="rating",
            tag="tag",
        )
        assert_matches_type(GiffffGetRandomResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_random(self, client: Giphy2) -> None:
        response = client.giffffs.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = response.parse()
        assert_matches_type(GiffffGetRandomResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_random(self, client: Giphy2) -> None:
        with client.giffffs.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = response.parse()
            assert_matches_type(GiffffGetRandomResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_trending(self, client: Giphy2) -> None:
        giffff = client.giffffs.get_trending()
        assert_matches_type(GiffffGetTrendingResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_trending_with_all_params(self, client: Giphy2) -> None:
        giffff = client.giffffs.get_trending(
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(GiffffGetTrendingResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_trending(self, client: Giphy2) -> None:
        response = client.giffffs.with_raw_response.get_trending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = response.parse()
        assert_matches_type(GiffffGetTrendingResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_trending(self, client: Giphy2) -> None:
        with client.giffffs.with_streaming_response.get_trending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = response.parse()
            assert_matches_type(GiffffGetTrendingResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: Giphy2) -> None:
        giffff = client.giffffs.search(
            q="q",
        )
        assert_matches_type(GiffffSearchResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_with_all_params(self, client: Giphy2) -> None:
        giffff = client.giffffs.search(
            q="q",
            lang="lang",
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(GiffffSearchResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: Giphy2) -> None:
        response = client.giffffs.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = response.parse()
        assert_matches_type(GiffffSearchResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: Giphy2) -> None:
        with client.giffffs.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = response.parse()
            assert_matches_type(GiffffSearchResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_translate(self, client: Giphy2) -> None:
        giffff = client.giffffs.translate(
            s="s",
        )
        assert_matches_type(GiffffTranslateResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_translate(self, client: Giphy2) -> None:
        response = client.giffffs.with_raw_response.translate(
            s="s",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = response.parse()
        assert_matches_type(GiffffTranslateResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_translate(self, client: Giphy2) -> None:
        with client.giffffs.with_streaming_response.translate(
            s="s",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = response.parse()
            assert_matches_type(GiffffTranslateResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGiffffs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.retrieve(
            0,
        )
        assert_matches_type(GiffffRetrieveResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.giffffs.with_raw_response.retrieve(
            0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = await response.parse()
        assert_matches_type(GiffffRetrieveResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncGiphy2) -> None:
        async with async_client.giffffs.with_streaming_response.retrieve(
            0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = await response.parse()
            assert_matches_type(GiffffRetrieveResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.list()
        assert_matches_type(GiffffListResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.list(
            ids="ids",
        )
        assert_matches_type(GiffffListResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.giffffs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = await response.parse()
        assert_matches_type(GiffffListResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncGiphy2) -> None:
        async with async_client.giffffs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = await response.parse()
            assert_matches_type(GiffffListResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_random(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.get_random()
        assert_matches_type(GiffffGetRandomResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_random_with_all_params(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.get_random(
            rating="rating",
            tag="tag",
        )
        assert_matches_type(GiffffGetRandomResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_random(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.giffffs.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = await response.parse()
        assert_matches_type(GiffffGetRandomResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_random(self, async_client: AsyncGiphy2) -> None:
        async with async_client.giffffs.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = await response.parse()
            assert_matches_type(GiffffGetRandomResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_trending(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.get_trending()
        assert_matches_type(GiffffGetTrendingResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_trending_with_all_params(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.get_trending(
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(GiffffGetTrendingResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_trending(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.giffffs.with_raw_response.get_trending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = await response.parse()
        assert_matches_type(GiffffGetTrendingResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_trending(self, async_client: AsyncGiphy2) -> None:
        async with async_client.giffffs.with_streaming_response.get_trending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = await response.parse()
            assert_matches_type(GiffffGetTrendingResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.search(
            q="q",
        )
        assert_matches_type(GiffffSearchResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.search(
            q="q",
            lang="lang",
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(GiffffSearchResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.giffffs.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = await response.parse()
        assert_matches_type(GiffffSearchResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncGiphy2) -> None:
        async with async_client.giffffs.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = await response.parse()
            assert_matches_type(GiffffSearchResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_translate(self, async_client: AsyncGiphy2) -> None:
        giffff = await async_client.giffffs.translate(
            s="s",
        )
        assert_matches_type(GiffffTranslateResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_translate(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.giffffs.with_raw_response.translate(
            s="s",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        giffff = await response.parse()
        assert_matches_type(GiffffTranslateResponse, giffff, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_translate(self, async_client: AsyncGiphy2) -> None:
        async with async_client.giffffs.with_streaming_response.translate(
            s="s",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            giffff = await response.parse()
            assert_matches_type(GiffffTranslateResponse, giffff, path=["response"])

        assert cast(Any, response.is_closed) is True
