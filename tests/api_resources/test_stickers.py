# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from giphy import Giphy2, AsyncGiphy2
from giphy.types import (
    StickerSearchResponse,
    StickerGetRandomResponse,
    StickerTranslateResponse,
    StickerGetTrendingResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStickers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_random(self, client: Giphy2) -> None:
        sticker = client.stickers.get_random()
        assert_matches_type(StickerGetRandomResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_random_with_all_params(self, client: Giphy2) -> None:
        sticker = client.stickers.get_random(
            rating="rating",
            tag="tag",
        )
        assert_matches_type(StickerGetRandomResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_random(self, client: Giphy2) -> None:
        response = client.stickers.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sticker = response.parse()
        assert_matches_type(StickerGetRandomResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_random(self, client: Giphy2) -> None:
        with client.stickers.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sticker = response.parse()
            assert_matches_type(StickerGetRandomResponse, sticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get_trending(self, client: Giphy2) -> None:
        sticker = client.stickers.get_trending()
        assert_matches_type(StickerGetTrendingResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_get_trending_with_all_params(self, client: Giphy2) -> None:
        sticker = client.stickers.get_trending(
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(StickerGetTrendingResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get_trending(self, client: Giphy2) -> None:
        response = client.stickers.with_raw_response.get_trending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sticker = response.parse()
        assert_matches_type(StickerGetTrendingResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get_trending(self, client: Giphy2) -> None:
        with client.stickers.with_streaming_response.get_trending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sticker = response.parse()
            assert_matches_type(StickerGetTrendingResponse, sticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_search(self, client: Giphy2) -> None:
        sticker = client.stickers.search(
            q="q",
        )
        assert_matches_type(StickerSearchResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_search_with_all_params(self, client: Giphy2) -> None:
        sticker = client.stickers.search(
            q="q",
            lang="lang",
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(StickerSearchResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_search(self, client: Giphy2) -> None:
        response = client.stickers.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sticker = response.parse()
        assert_matches_type(StickerSearchResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_search(self, client: Giphy2) -> None:
        with client.stickers.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sticker = response.parse()
            assert_matches_type(StickerSearchResponse, sticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_translate(self, client: Giphy2) -> None:
        sticker = client.stickers.translate(
            s="s",
        )
        assert_matches_type(StickerTranslateResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_translate(self, client: Giphy2) -> None:
        response = client.stickers.with_raw_response.translate(
            s="s",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sticker = response.parse()
        assert_matches_type(StickerTranslateResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_translate(self, client: Giphy2) -> None:
        with client.stickers.with_streaming_response.translate(
            s="s",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sticker = response.parse()
            assert_matches_type(StickerTranslateResponse, sticker, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStickers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_random(self, async_client: AsyncGiphy2) -> None:
        sticker = await async_client.stickers.get_random()
        assert_matches_type(StickerGetRandomResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_random_with_all_params(self, async_client: AsyncGiphy2) -> None:
        sticker = await async_client.stickers.get_random(
            rating="rating",
            tag="tag",
        )
        assert_matches_type(StickerGetRandomResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_random(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.stickers.with_raw_response.get_random()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sticker = await response.parse()
        assert_matches_type(StickerGetRandomResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_random(self, async_client: AsyncGiphy2) -> None:
        async with async_client.stickers.with_streaming_response.get_random() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sticker = await response.parse()
            assert_matches_type(StickerGetRandomResponse, sticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_trending(self, async_client: AsyncGiphy2) -> None:
        sticker = await async_client.stickers.get_trending()
        assert_matches_type(StickerGetTrendingResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_get_trending_with_all_params(self, async_client: AsyncGiphy2) -> None:
        sticker = await async_client.stickers.get_trending(
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(StickerGetTrendingResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get_trending(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.stickers.with_raw_response.get_trending()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sticker = await response.parse()
        assert_matches_type(StickerGetTrendingResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get_trending(self, async_client: AsyncGiphy2) -> None:
        async with async_client.stickers.with_streaming_response.get_trending() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sticker = await response.parse()
            assert_matches_type(StickerGetTrendingResponse, sticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_search(self, async_client: AsyncGiphy2) -> None:
        sticker = await async_client.stickers.search(
            q="q",
        )
        assert_matches_type(StickerSearchResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncGiphy2) -> None:
        sticker = await async_client.stickers.search(
            q="q",
            lang="lang",
            limit=0,
            offset=0,
            rating="rating",
        )
        assert_matches_type(StickerSearchResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.stickers.with_raw_response.search(
            q="q",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sticker = await response.parse()
        assert_matches_type(StickerSearchResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncGiphy2) -> None:
        async with async_client.stickers.with_streaming_response.search(
            q="q",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sticker = await response.parse()
            assert_matches_type(StickerSearchResponse, sticker, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_translate(self, async_client: AsyncGiphy2) -> None:
        sticker = await async_client.stickers.translate(
            s="s",
        )
        assert_matches_type(StickerTranslateResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_translate(self, async_client: AsyncGiphy2) -> None:
        response = await async_client.stickers.with_raw_response.translate(
            s="s",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sticker = await response.parse()
        assert_matches_type(StickerTranslateResponse, sticker, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_translate(self, async_client: AsyncGiphy2) -> None:
        async with async_client.stickers.with_streaming_response.translate(
            s="s",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sticker = await response.parse()
            assert_matches_type(StickerTranslateResponse, sticker, path=["response"])

        assert cast(Any, response.is_closed) is True
