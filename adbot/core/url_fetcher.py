import nest_asyncio

from adbot.misc.collections import URLCollection


class URLFetcher:
    nest_asyncio.apply()

    def crawl(self, website: Website) -> URLCollection:
    """TODO: Change to stop locating when know new urls were found"""

    with URLCollection(website=website) as collection:
        collection += asyncio.run(fetch_links(urls=[website.url.url]))
    return collection
