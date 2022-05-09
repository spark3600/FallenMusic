from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","𓆩♥️𓆪 𝙍𝘼𝘾𝙃𝙉𝘼 𝙈𝙐𝙎𝙄𝘾 ⧉⃞꯭♥️━━")
BOT_USERNAME = getenv("BOT_USERNAME", "Rachna_MusicBot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "near16")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "world_of_telegramer")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/2624e48e0ad4e29d184c5.jpg")
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/2624e48e0ad4e29d184c5.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1844115387").split()))
