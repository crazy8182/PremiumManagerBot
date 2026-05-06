from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
import asyncio

from utils.checker import premium_checker
from utils.reminders import left_group_checker

app = Client(
    "PremiumManagerBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def main():

    await app.start()

    print("Premium Bot Started")

    asyncio.create_task(premium_checker(app))
    asyncio.create_task(left_group_checker(app))

    await idle()

    await app.stop()

app.run(main())
