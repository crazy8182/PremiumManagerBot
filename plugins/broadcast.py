from pyrogram import Client, filters
from config import ADMIN_ID
from database.premium import get_all_users

@Client.on_message(filters.command("broadcast") & filters.user(ADMIN_ID))
async def broadcast(client, message):

    if not message.reply_to_message:
        return await message.reply_text("Reply to a message")

    users = await get_all_users()

    done = 0

    for user in users:
        try:
            await message.reply_to_message.copy(user["user_id"])
            done += 1
        except:
            pass

    await message.reply_text(f"Broadcast Sent To: {done}")
