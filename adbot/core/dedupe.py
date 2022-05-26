from typing import List

from adbot.misc.website import URL


class URLCollection:
    def __init__(self, urls: List[URL]) -> None:
        self._urls = urls

    @property
    def urls(self) -> List[URL]:
        return self._urls

    def __len__(self) -> int:
        return len(self._urls)

    def __iter__(self) -> None:
        for url in self._urls:
            return url

    def __add__(self, urls: List[URL]) -> None:
        if not isinstance(urls, list):
            raise ValueError(f"{urls} is not a list but {type(urls)}")
        self._urls + urls
        self.dedupe()

    def dedupe(self) -> None:
        self._urls = list(set(self._urls))
