import requests
from tqdm import tqdm

from adbot.conf.logging import logger
from adbot.misc.files import Video


def download_video(video: Video) -> None:
    try:
        response = requests.get(video.src, stream=True, timeout=10)
        total_size_in_bytes = int(response.headers.get("content-length", 0))

        with tqdm(
            total=total_size_in_bytes, unit="iB", unit_scale=True
        ) as progress_bar:
            with open(video.name, "wb") as f:
                for chunk in tqdm(response.iter_content(chunk_size=1024)):
                    if chunk:
                        progress_bar.update(len(chunk))
                        f.write(chunk)
                        # f.flush()

            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                logger.error(f"[Error] The download of {video.src} failed")
                return
        logger.info(f"[Download] {video.src} downloaded successfully")

    except Exception as e:
        logger.error(f"[Error] {e}")
