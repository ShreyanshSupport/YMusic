import os


API_ID: int = int(os.getenv("API_ID", 0))

API_HASH: str = os.getenv("API_HASH", "")

SESSION_STRING: str = os.getenv("SESSION_STRING", "")

app_version: str = os.getenv ("userbot_version", "")

device_model": str = os.getenv ("f"Moon-Userbot @ {gitrepo.head.commit.hexsha[:7]}", "")

system_version: str = os.getenv ("platform.version() + " " + platform.machine()" , "")

OWNER_ID: list[int] = [int(id.strip()) for id in os.getenv("OWNER_ID", "0").split(",")]

LOG_GROUP_ID: int = int(os.getenv("LOG_GROUP_ID", 0))

PREFIX: str = str(".")

RPREFIX: str = str("$")


# No Need To Edit Below This

LOG_FILE_NAME: str = "YMusic.txt"
