from adbot.misc.website import Website
from adbot.core.crawl import crawl
from adbot.conf.load_settings import load_settings


def main(uri: str) -> None:

    website = Website(uri)
    collection = crawl(website=website)
