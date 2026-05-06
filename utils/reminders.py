from database.premium import get_all_premium
from config import PREMIUM_GROUP_ID
import asyncio

async def left_group_checker(client):

    while True:

        users = await get_all_premium()

        for user in users:

            try:
                await client.get_chat_member(
                    PREMIUM_GROUP_ID,
                    user["user_id"]
                )

            except:

                try:
                    await client.send_message(
                        user["user_id"],
                        "⚠️ You left premium group. Contact admin to rejoin."
                    )
                except:
                    pass

        await asyncio.sleep(86400)
