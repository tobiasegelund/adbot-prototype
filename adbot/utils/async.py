import re
from typing import List

import asyncio
from aiohttp import ClientSession

from adbot.conf.logging import logger
from adbot.misc.website import URL, Website
from adbot.utils import flatten_lists
from adbot.misc.collections import URLCollection


async def fetch_url(url: URL, session: ClientSession) -> str:
    logger.info(f"[Info] Fetch {str(url)}")
    response = await session.request(method="GET", url=url)
    logger.info(f"[Info] {str(url)} responded with status code {response.status}")
    html = await response.text()
    return html


async def collect_links(html: str) -> List[str]:
    href = re.compile(r'href="(.*?)"')
    _links = list(link for link in href.findall(html))
    return _links


async def fetch_links(urls: List[URL]) -> List[str]:
    """
    Usage:
        output = asyncio.run(fetch_links(urls=urls))
    """
    links = list()

    async def update_links(url: URL, session: ClientSession) -> None:

        html = await fetch_url(url=url, session=session)
        links = await collect_links(html=html)
        logger.info(f"[Info] On {str(url)} {len(links)} links were found")
        return links

    async with ClientSession() as session:
        tasks = list(update_links(url=url, session=session) for url in urls)
        _links = await asyncio.gather(*tasks)
        links += _links
    return flatten_lists(list_of_lists=links)


def crawl(website: Website) -> URLCollection:
    """TODO: Change to stop locating when know new urls were found"""

    with URLCollection(website=website) as collection:
        collection += asyncio.run(fetch_links(urls=[website.url.url]))
    return collection
