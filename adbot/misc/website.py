import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from adbot.utils.exceptions import NotURLObject


class URL:
    """Class to represent a URL

    The class will construct the URL itself, if it's initialized with the URI.
    It is possible to use the object as input string for URL.
    """

    def __init__(self, uri: str) -> None:
        self._url = self._contruct_url(uri)

    def __hash__(self) -> None:
        return hash(self._url)

    def __add__(self, val: str) -> None:
        if not isinstance(val, str):
            raise ValueError(f"Input is not a string but {type(val)}")
        self._url += val

    def __eq__(self, obj) -> None:
        return isinstance(obj, URL) and self._url == obj.url

    def __str__(self) -> str:
        return self._url

    def __repr__(self) -> str:
        return f"URL<{self.url}>"

    @property
    def url(self) -> str:
        return self._url

    def _contruct_url(self, uri: str) -> None:
        return self._add_scheme(uri)

    def _add_scheme(self, uri: str) -> str:
        if uri[: len("https://")] != "https://":
            return "https://" + uri
        return uri


class Website:
    def __init__(self, url: URL) -> None:
        self._url = url
        self._parsed_url = urlparse(str(url))

    @property
    def url(self) -> str:
        return self._url

    @property
    def scheme(self) -> str:
        return self._parsed_url.scheme

    @property
    def domain(self) -> str:
        return self._parsed_url.hostname

    @property
    def netloc(self) -> str:
        return (
            self._parsed_url.netloc[4:]
            if self._parsed_url.netloc[:4] == "www."
            else self._parsed_url.netloc
        )
