import datetime
import logging

from adbot import DIR_LOG

logging.basicConfig(
    filename=DIR_LOG.joinpath(f"{datetime.datetime.today()}.log"),
    filemode="w",
    format="%(asctime)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)
