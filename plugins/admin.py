from pyrogram import Client, filters
from config import ADMIN_ID
from database.premium import get_all_premium

@Client.on_message(filters.command("stats") & filters.user(ADMIN_ID))
async def stats(client, message):

    users = await get_all_premium()

    await message.reply_text(
        f"Premium Users: {len(users)}"
    )
