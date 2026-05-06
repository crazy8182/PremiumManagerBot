from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.premium import add_user

TEXT = '''
🔥 Premium Membership Plans

🥇 1 Month - ₹99
🥈 3 Month - ₹249
🏆 6 Month - ₹449
💎 1 Year - ₹799
'''

@Client.on_message(filters.command("start"))
async def start(client, message):

    await add_user(message.from_user.id)

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("💳 Buy Premium", callback_data="buy")],
        [InlineKeyboardButton("👑 My Plan", callback_data="myplan")]
    ])

    await message.reply_text(TEXT, reply_markup=buttons)
