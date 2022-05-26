class TestURL:
    def test_add(self, url):
        url + "/new"
        assert str(url) == "https://tv2.dk/new"


class TestWebsite:
    pass
