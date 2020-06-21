import logging
from pathlib import Path

from envparse import env


def setup_logger(logger):

    logger.setLevel(logging.DEBUG)
    stream_handler = logging.StreamHandler()
    formatter = logging.Formatter("[%(asctime)s] - %(message)s", datefmt="%d.%m %H:%M:%S")
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


env_path = Path(__file__).parent.parent / ".env"
env.read_envfile(path=env_path.as_posix())

BOT_TOKEN = env.str("BOT_TOKEN")
