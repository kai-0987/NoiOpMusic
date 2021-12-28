##Config

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
