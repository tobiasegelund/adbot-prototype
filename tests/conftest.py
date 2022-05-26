import pytest
from adbot.misc.website import URL, Website


@pytest.fixture(scope="session")
def url():
    yield URL("tv2.dk")
