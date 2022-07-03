import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")
que = {}
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5357340564").split()))
API_ID = int(getenv("API_ID", "13722517"))
API_HASH = getenv("API_HASH", "842b6009730ea97f4b2716bd4b6ada71")
LOG_CHAT = int(getenv("LOG_CHAT", "-1001630621701"))
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_USERNAME = getenv("SPOTIFY_USERNAME")
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Oyehoye143:Oyehoye143@cluster0.y12dk.mongodb.net/?retryWrites=true&w=majority")
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/d96299aa8c8efa11a59cc.jpg")
DB_URL = getenv("DATABASE_URL", "")
STRING_SESSION1 = getenv("STRING_SESSION1", "BQCsLmYD4WGqzjIe2wHK81aVFWn4nQ9FEZsKXfTGIjKIl3rQltK1XnlUZJdlNog2EoEYX9ERCbxI4pvwqCEvbSxOPcdCl8ga2gecSSEYOxsjf2miqbX-v0RqAfS3qy21uKHKIquwvvLJ3OZlnKISl0NXfMOabFVRNSkZMuvTivxzmhGrLFYWjXWzTikre8BbA5Urhtwn1FTIeayKFBbSyUVS1p52Dt3q0aNo1sMiuUxc5DlMomfLWc9BT8BsXqKWdgEYZqC_P8y7p7aJVr8npqTqsZGc-5QJVdfCBB4_pHzjmdKrf2IDXZvubU7zPhTGbpjVJuvkOsGeDHVz0cZwALnrAAAAAT9Sh5QA")
STRING_
