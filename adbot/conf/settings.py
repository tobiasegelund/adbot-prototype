from typing import Any, Dict

import yaml
from selenium import webdriver

from adbot import DIR_SETTINGS
from adbot.utils.exceptions import SettingNotFound, WrongEnvironment
from adbot.misc.website import URL


class Settings:
    """Class to represent the settings and environment of ads to download

    Args:
        file, Dict[str, Any]: A dictionary file with stored settings

    Examples:
        >>> settings = Settings.load("template")
    """

    def __init__(self, file: Dict[str, Any]) -> None:
        for key, val in file.items():
            setattr(self, key, val)

        self.url = URL(uri=self.domain)

    def __repr__(self) -> str:
        return f"Settings<{self.domain}>"

    @property
    def environment(self) -> None:
        return self._environment

    @environment.setter
    def environment(self, val) -> None:
        if (env := val.lower()) not in ("production", "development", "test"):
            raise WrongEnvironment(
                "Environment must be production, development or test"
            )

        self.options = webdriver.FirefoxOptions()
        if env in ("production", "test"):
            self.options.add_argument("--headless")
            self.options.add_argument("--no-sandbox")

        self._environment = env

    def __getattr__(self, key: str) -> Any:
        if val := self.__dict__.get(key, None) is None:
            raise SettingNotFound(f"No setting called {key}")
        return val

    @classmethod
    def load(cls, domain: str):
        filename = domain + ".yml"
        path = DIR_SETTINGS.joinpath(filename)

        if path.exists():
            with open(path, mode="r", encoding="utf-8") as f:
                file = yaml.safe_load(f)
        else:
            raise FileNotFoundError(
                f"There exists no file called {domain}.yml in the folder of settings"
            )

        return cls(file=file)
