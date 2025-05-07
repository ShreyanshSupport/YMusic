from pyrogram import Client
from pytgcalls import PyTgCalls

import platform
from utils import config
from utils.misc import gitrepo, userbot_version

api_id: int = config.API_ID
api_hash: str = config.API_HASH
session_string: str = config.SESSION_STRING

YMusicBot = Client(
    name="YMusic",
    api_id=api_id,
    api_hash=api_hash,
    session_string=session_string,
    device_model=f"YMusic-Userbot @ {gitrepo.head.commit.hexsha[:7]}",
    system_version=platform.version() + " " + platform.machine(),
    app_version=userbot_version,
    workdir="./",
    sleep_threshold=10,
    parse_mode="html"
)

YMusicUser = PyTgCalls(YMusicBot)
