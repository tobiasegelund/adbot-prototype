from pathlib import Path
from typing import Any

import yaml

from adbot import DIR_SETTINGS
from adbot.utils.exceptions import SettingNotFound, WrongEnvironment


class Settings:
    """Class to represent the settings and environment of ads to download

    Args:
        path, pathlib.Path: The path to settings
    """

    def __init__(self, path: Path) -> None:
        self._load_settings(path=path)

    @property
    def environment(self) -> None:
        return self._environment

    @environment.setter
    def environment(self, val) -> None:
        if (env := val.lower()) not in ("production", "development", "test"):
            raise WrongEnvironment(
                "Environment must be production, development or test"
            )
        self._environment = env

    def __getattr__(self, key: str) -> Any:
        if val := self.__dict__[key] is None:
            raise SettingNotFound(f"{key} setting cannot be found")
        return val

    def _load_settings(self, path: Path) -> None:
        with open(path, mode="r", encoding="utf-8") as f:
            file = yaml.safe_load(f)

        for key, val in file.items():
            setattr(self, key, val)


def load_settings(ctx: str) -> Settings:
    contexts = {"default": DIR_SETTINGS.joinpath("default.yml")}

    try:
        path = contexts[ctx]
    except KeyError:
        path = contexts["defualt"]

    settings = Settings(path=path)

    return settings
