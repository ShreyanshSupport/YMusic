from pyrogram import Client
from pytgcalls import PyTgCalls

import config
from ..logging import LOGGER

api_id: int = config.API_ID
api_hash: str = config.API_HASH
session_string: str = config.SESSION_STRING
app_version: str = config.userbot_version
device_model: str = config.f"KittyBeats @ {gitrepo.head.commit.hexsha[:7]}"
system_version: str = config.platform.version() + " " + platform.machine()

YMusicBot = Client(
    name="YMusic", api_id=api_id, api_hash=api_hash, session_string=session_string app_version:userbot_version
device_model:f"KittyBeats @ {gitrepo.head.commit.hexsha[:7]}"
system_version:platform.version() + " " + platform.machine()
)

YMusicUser = PyTgCalls(YMusicBot)
