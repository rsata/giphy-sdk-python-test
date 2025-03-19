# Gifs

Types:

```python
from giphy.types import (
    Gif,
    Image,
    Meta,
    Pagination,
    GifRetrieveResponse,
    GifListResponse,
    GifGetRandomResponse,
    GifGetTrendingResponse,
    GifSearchResponse,
    GifTranslateResponse,
)
```

Methods:

- <code title="get /gifs/{gifId}">client.gifs.<a href="./src/giphy/resources/gifs.py">retrieve</a>(gif_id) -> <a href="./src/giphy/types/gif_retrieve_response.py">GifRetrieveResponse</a></code>
- <code title="get /gifs">client.gifs.<a href="./src/giphy/resources/gifs.py">list</a>(\*\*<a href="src/giphy/types/gif_list_params.py">params</a>) -> <a href="./src/giphy/types/gif_list_response.py">GifListResponse</a></code>
- <code title="get /gifs/random">client.gifs.<a href="./src/giphy/resources/gifs.py">get_random</a>(\*\*<a href="src/giphy/types/gif_get_random_params.py">params</a>) -> <a href="./src/giphy/types/gif_get_random_response.py">GifGetRandomResponse</a></code>
- <code title="get /gifs/trending">client.gifs.<a href="./src/giphy/resources/gifs.py">get_trending</a>(\*\*<a href="src/giphy/types/gif_get_trending_params.py">params</a>) -> <a href="./src/giphy/types/gif_get_trending_response.py">GifGetTrendingResponse</a></code>
- <code title="get /gifs/search">client.gifs.<a href="./src/giphy/resources/gifs.py">search</a>(\*\*<a href="src/giphy/types/gif_search_params.py">params</a>) -> <a href="./src/giphy/types/gif_search_response.py">GifSearchResponse</a></code>
- <code title="get /gifs/translate">client.gifs.<a href="./src/giphy/resources/gifs.py">translate</a>(\*\*<a href="src/giphy/types/gif_translate_params.py">params</a>) -> <a href="./src/giphy/types/gif_translate_response.py">GifTranslateResponse</a></code>

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
