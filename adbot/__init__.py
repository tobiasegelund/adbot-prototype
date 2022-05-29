from pathlib import Path
import os


DIR_ROOT = Path(os.path.dirname(os.path.abspath(__file__)))
DIR_BASE = DIR_ROOT.parent
DIR_SETTINGS = DIR_ROOT.joinpath("settings")
DIR_LOG = DIR_BASE.joinpath("LOGS")
DIR_FILES = DIR_BASE.joinpath("FILES")

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
}
