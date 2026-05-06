from pyrogram import Client, filters
from pyrogram.types import *
from config import *
from datetime import datetime, timedelta
from database.premium import add_premium

pending = {}

@Client.on_callback_query(filters.regex("buy"))
async def buy_menu(client, query):

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("1 Month", callback_data="plan_1month")],
        [InlineKeyboardButton("3 Month", callback_data="plan_3month")],
        [InlineKeyboardButton("6 Month", callback_data="plan_6month")],
        [InlineKeyboardButton("1 Year", callback_data="plan_12month")]
    ])

    await query.message.reply_text(
        "Select Premium Plan",
        reply_markup=buttons
    )

@Client.on_callback_query(filters.regex("plan"))
async def plan_select(client, query):

    plan = query.data.split("_")[1]
    pending[query.from_user.id] = plan
    data = PLANS[plan]

    text = f'''
💳 Payment Information

UPI ID:
`{UPI_ID}`

Amount: ₹{data["price"]}

After payment send screenshot.
'''

    await client.send_photo(
        query.from_user.id,
        QR_IMAGE,
        caption=text
    )

@Client.on_message(filters.photo)
async def payment_ss(client, message):

    if message.from_user.id not in pending:
        return

    await message.forward(ADMIN_ID[0])

    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "✅ Approve",
                callback_data=f"approve_{message.from_user.id}"
            ),
            InlineKeyboardButton(
                "❌ Reject",
                callback_data=f"reject_{message.from_user.id}"
            )
        ]
    ])

    await client.send_message(
        ADMIN_ID[0],
        f"Payment Verification\n\nUser ID: {message.from_user.id}",
        reply_markup=buttons
    )

@Client.on_callback_query(filters.regex("approve"))
async def approve(client, query):

    user_id = int(query.data.split("_")[1])
    plan = pending[user_id]
    days = PLANS[plan]["days"]

    expiry = datetime.now() + timedelta(days=days)

    user = await client.get_users(user_id)

    await add_premium(
        user_id,
        user.first_name,
        PLANS[plan]["name"],
        expiry
    )

    invite = await client.create_chat_invite_link(
        PREMIUM_GROUP_ID,
        member_limit=1
    )

    await client.send_message(
        user_id,
        f'''
✅ Premium Activated

Plan: {PLANS[plan]["name"]}
Expiry: {expiry.date()}

Join Group:
{invite.invite_link}
'''
    )

    await query.message.edit_text("Approved")

@Client.on_callback_query(filters.regex("reject"))
async def reject(client, query):

    user_id = int(query.data.split("_")[1])

    await client.send_message(
        user_id,
        "❌ Payment Rejected"
    )

    await query.message.edit_text("Rejected")
