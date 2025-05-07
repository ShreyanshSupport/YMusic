from pyrogram import Client
from pytgcalls import PyTgCalls

import config
import platform
from ..logging import LOGGER

api_id: int = config.API_ID
api_hash: str = config.API_HASH
session_string: str = config.SESSION_STRING

# Hardcoded values
userbot_version = "2.5.0"
device_model = "kittuBeats-Userbot @Tech_Shreuansh29"
system_version = f"{platform.system()} {platform.release()} {platform.machine()}"

YMusicBot = Client(
    name="YMusic",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string,
    device_model=device_model,
    system_version=system_version,
    app_version=userbot_version,
    workdir="./",
    sleep_threshold=10,
    parse_mode="html"
)

YMusicUser = PyTgCalls(YMusicBot)
