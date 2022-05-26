import re
from typing import List

import nest_asyncio
import asyncio
from aiohttp import ClientSession

from adbot.conf.logging import logger
from adbot.misc.website import URL


nest_asyncio.apply()


def dedupe_urls(urls: List[URL]) -> List[URL]:
    return list(set(urls))


def create_url_objects(links: List[str]) -> List[URL]:
    return list(URL(uri=link) for link in links)


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
        global links

        html = await fetch_url(url=url, session=session)
        _links = await collect_links(html=html)
        logger.info(f"[Info] On {str(url)} {len(_links)} links were found")
        links += links + _links

    async with ClientSession() as session:
        tasks = list(update_links(url=url, session=session) for url in urls)
        await asyncio.gather(*tasks)

    return links


def crawl(urls: List[URL], links: List[URL] = []) -> List[URL]:
    if len(urls) > 0:
        links = asyncio.run(fetch_links(urls=urls))
        urls = dedupe_urls(urls=links)
        links = crawl(urls=urls, links=links)

    return links
