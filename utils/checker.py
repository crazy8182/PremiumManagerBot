from database.premium import get_all_premium, remove_premium
from datetime import datetime
from config import PREMIUM_GROUP_ID, ADMIN_ID
import asyncio

async def premium_checker(client):

    while True:

        users = await get_all_premium()

        for user in users:

            expiry = user["expiry"]

            if datetime.now() > expiry:

                try:
                    await client.ban_chat_member(
                        PREMIUM_GROUP_ID,
                        user["user_id"]
                    )

                    await client.unban_chat_member(
                        PREMIUM_GROUP_ID,
                        user["user_id"]
                    )

                except:
                    pass

                await client.send_message(
                    ADMIN_ID[0],
                    f"Premium Expired: {user['name']}"
                )

                await remove_premium(user["user_id"])

        await asyncio.sleep(3600)
