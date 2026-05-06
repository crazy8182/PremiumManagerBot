from pyrogram import Client, filters
from database.premium import get_premium

@Client.on_callback_query(filters.regex("myplan"))
async def my_plan(client, query):

    user = await get_premium(query.from_user.id)

    if not user:
        return await query.message.reply_text("No Active Premium")

    text = f'''
👑 Premium Active

Plan: {user["plan"]}
Expiry: {user["expiry"].date()}
'''

    await query.message.reply_text(text)
