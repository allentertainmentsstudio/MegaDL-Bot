# (c) Asm Safone
# A Part of MegaDL-Bot <https://github.com/AsmSafone/MegaDL-Bot>


import os

class Config:
    API_ID = int(os.environ.get("API_ID", 34446649))
    API_HASH = os.environ.get("API_HASH", "8dc570c08d8e35e88fb9bfc73c65d7fa")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8799486461:AAH6td7_S68a3PnGNJermUgxA6_A1vhBS-c")
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    TG_MAX_SIZE = 2040108421
    OWNER_ID = int(os.environ.get("OWNER_ID", 7892805795))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1003515041061))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", -1003758676689))


class TEXT:
  ABOUT = """
🤖 **Name:** Mega Downloader Bot

📝 **Language:** [Python](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted On:** [Heroku](https://heroku.com)

🧑‍💻 **Developer:** [Anuj](https://t.me/anujedits76)

👥 **Support Group:** [Anuj Kumar](https://t.me/log_channel_a)

📢 **Updates Channel:** [Anuj Kumar](https://t.me/log_channel_a)
"""

  HELP_USER = """
This is **Mega Downloader Bot**

This Bot Can Download Files & Videos From Mega Links & Upload To Telegram. Just Send Any Mega.nz Link & See The Magic. You Can Also Add or Change Caption: Just Select An Uploaded File/ Video or Forward Me Any Telegram File & Then Write The Text You Want To Be Caption On The File As A Reply To That File & The Text You Wrote Will Be Attached As Caption 😁! 

**Made With ❤️ By @anujedits76! 👑**
"""

  START_TEXT = """
👋🏻 **Hi** {user_mention},

I'm **{bot_name}**
I Can Download Files & Videos From Mega.nz Links & Upload To Telegram. Please Check Help To Learn More 😉!

**Maintained By: @anujedits76**❤️!
"""
