from mmpy_bot.bot import Bot
import os

if __name__ == "__main__":
    os.environ.setdefault("MATTERMOST_BOT_SETTINGS_MODULE", "mmpy_bot_settings")

    Bot().run()
