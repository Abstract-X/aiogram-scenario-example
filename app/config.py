from pathlib import Path

from envparse import env


env_path = Path(__file__).parent.parent / ".env"
env.read_envfile(path=env_path.as_posix())

BOT_TOKEN = env.str("BOT_TOKEN")
