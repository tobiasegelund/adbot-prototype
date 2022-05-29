from typing import List

from adbot.misc.website import URL
from adbot.conf.load_settings import Settings


class URLCollection:
    def __init__(self, settings: Settings, *, urls: List[URL] = []) -> None:
        self._urls = urls
        self._settings = settings

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        self.dedupe()

    @property
    def urls(self) -> List[URL]:
        return self._urls

    def __len__(self) -> int:
        return len(self._urls)

    def __iter__(self) -> None:
        for url in self._urls:
            return url

    def __add__(self, links: List[str]) -> None:
        if not isinstance(links, list):
            raise ValueError(f"{links} is not a list but {type(links)}")
        urls = self.create_url_objects(links)
        self._urls + urls
        self.dedupe()

    def create_url_objects(self, links: List[str]) -> List[URL]:
        return list(URL(uri=link) for link in links)

    def dedupe(self) -> None:
        self._urls = list(set(self._urls))
