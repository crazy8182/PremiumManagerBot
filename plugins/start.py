from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database.premium import add_user

TEXT = '''
🔥 Premium Membership Plans

🥇 1 Month - ₹69
🥈 3 Month - ₹179
🏆 6 Month - ₹299
💎 1 Year - ₹549
'''

@Client.on_message(filters.command("start"))
async def start(client, message):

    await add_user(message.from_user.id)

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("💳 Buy Premium", callback_data="buy")],
        [InlineKeyboardButton("👑 My Plan", callback_data="myplan")]
    ])

    await message.reply_text(reply_markup=buttons)
