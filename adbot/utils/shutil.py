from pathlib import Path


def create_dir_if_not_exits(dir_name: Path, force: bool = False) -> None:
    dir_name.mkdir(parents=True, exist_ok=True)
