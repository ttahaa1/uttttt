from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://i.pinimg.com/originals/98/c5/28/98c528ee2c22dbfb3fb20e56854b9871.jpg")
START_IMG = getenv("START_IMG", "https://i.pinimg.com/originals/98/c5/28/98c528ee2c22dbfb3fb20e56854b9871.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/z_gsx")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/b1o_d_a")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6264668799").split()))


FAILED = "https://i.pinimg.com/originals/98/c5/28/98c528ee2c22dbfb3fb20e56854b9871.jpg"
