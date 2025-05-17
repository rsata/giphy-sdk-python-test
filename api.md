# Giffffs

Types:

```python
from giphy.types import (
    Gif,
    Image,
    Meta,
    Pagination,
    GiffffRetrieveResponse,
    GiffffListResponse,
    GiffffGetRandomResponse,
    GiffffGetTrendingResponse,
    GiffffSearchResponse,
    GiffffTranslateResponse,
)
```

Methods:

- <code title="get /gifs/{gifId}">client.giffffs.<a href="./src/giphy/resources/giffffs.py">retrieve</a>(gif_id) -> <a href="./src/giphy/types/giffff_retrieve_response.py">GiffffRetrieveResponse</a></code>
- <code title="get /gifs">client.giffffs.<a href="./src/giphy/resources/giffffs.py">list</a>(\*\*<a href="src/giphy/types/giffff_list_params.py">params</a>) -> <a href="./src/giphy/types/giffff_list_response.py">GiffffListResponse</a></code>
- <code title="get /gifs/random">client.giffffs.<a href="./src/giphy/resources/giffffs.py">get_random</a>(\*\*<a href="src/giphy/types/giffff_get_random_params.py">params</a>) -> <a href="./src/giphy/types/giffff_get_random_response.py">GiffffGetRandomResponse</a></code>
- <code title="get /gifs/trending">client.giffffs.<a href="./src/giphy/resources/giffffs.py">get_trending</a>(\*\*<a href="src/giphy/types/giffff_get_trending_params.py">params</a>) -> <a href="./src/giphy/types/giffff_get_trending_response.py">GiffffGetTrendingResponse</a></code>
- <code title="get /gifs/search">client.giffffs.<a href="./src/giphy/resources/giffffs.py">search</a>(\*\*<a href="src/giphy/types/giffff_search_params.py">params</a>) -> <a href="./src/giphy/types/giffff_search_response.py">GiffffSearchResponse</a></code>
- <code title="get /gifs/translate">client.giffffs.<a href="./src/giphy/resources/giffffs.py">translate</a>(\*\*<a href="src/giphy/types/giffff_translate_params.py">params</a>) -> <a href="./src/giphy/types/giffff_translate_response.py">GiffffTranslateResponse</a></code>

# Stickers

Types:

```python
from giphy.types import (
    StickerGetRandomResponse,
    StickerGetTrendingResponse,
    StickerSearchResponse,
    StickerTranslateResponse,
)
```

Methods:

- <code title="get /stickers/random">client.stickers.<a href="./src/giphy/resources/stickers.py">get_random</a>(\*\*<a href="src/giphy/types/sticker_get_random_params.py">params</a>) -> <a href="./src/giphy/types/sticker_get_random_response.py">StickerGetRandomResponse</a></code>
- <code title="get /stickers/trending">client.stickers.<a href="./src/giphy/resources/stickers.py">get_trending</a>(\*\*<a href="src/giphy/types/sticker_get_trending_params.py">params</a>) -> <a href="./src/giphy/types/sticker_get_trending_response.py">StickerGetTrendingResponse</a></code>
- <code title="get /stickers/search">client.stickers.<a href="./src/giphy/resources/stickers.py">search</a>(\*\*<a href="src/giphy/types/sticker_search_params.py">params</a>) -> <a href="./src/giphy/types/sticker_search_response.py">StickerSearchResponse</a></code>
- <code title="get /stickers/translate">client.stickers.<a href="./src/giphy/resources/stickers.py">translate</a>(\*\*<a href="src/giphy/types/sticker_translate_params.py">params</a>) -> <a href="./src/giphy/types/sticker_translate_response.py">StickerTranslateResponse</a></code>
