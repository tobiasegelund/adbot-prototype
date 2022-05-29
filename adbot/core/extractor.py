import time
from typing import List, Any

from selenium.webdriver import Firefox
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.keys import Keys

from adbot import DIR_FILES
from adbot.misc.website import URL
from adbot.conf.settings import Settings
from adbot.utils.shutil import create_dir_if_not_exits


SCROLL_HEIGHT = 1000
SCROLL_PAUSE_TIME = 0.5


class Extractor:
    src: List[
        str
    ] = list()  # An empty list to store already downloaded / screenshotted src

    def __init__(self, urls: List[URL], settings: Settings) -> None:
        self.urls = urls
        self.settings = settings

    def _load_driver(self) -> None:
        self.driver = Firefox(options=self.settings.options)
        self.driver.get(str(self.settings.url))
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.settings.cookie))
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "iframe"))
        )

    def _get_tags(self) -> List[Any]:
        """TODO: Loop through all possible tags"""
        pass

    def _get_image_extensions(self) -> None:
        self.image_extensions = self.settings.files.get("image", None)

    def _get_video_extensions(self) -> None:
        self.video_extensions = self.settings.files.get("video", None)

    def _scroll_page_slowly(self) -> None:
        """Render page slowly"""
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        iterations = (total_height // SCROLL_HEIGHT) + 1

        height = 1000
        for timer in range(0, iterations):
            self.driver.execute_script("window.scrollTo(0, " + str(height) + ")")
            height += SCROLL_HEIGHT
            time.sleep(SCROLL_PAUSE_TIME)

    def _create_folder(self) -> None:
        """TODO: Add option to store locally"""
        folder_name = DIR_FILES.joinpath(self.settings.domain)
        create_dir_if_not_exits(folder_name)

    def _run(self) -> None:
        for url in self.urls:
            self.driver.get(str(url))
            self._scroll_page_slowly()
