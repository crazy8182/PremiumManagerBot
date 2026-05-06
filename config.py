import os

API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

MONGO_URI = os.environ.get("MONGO_URI", "")

ADMIN_ID = [123456789]

PREMIUM_GROUP_ID = -1001234567890
LOG_CHANNEL = -1001234567890

UPI_ID = "yourname@upi"

QR_IMAGE = "assets/qr.png"

PLANS = {
    "1month": {"days": 30, "price": "99", "name": "Monthly"},
    "3month": {"days": 90, "price": "249", "name": "Quarterly"},
    "6month": {"days": 180, "price": "449", "name": "Haf-Yearly"},
    "12month": {"days": 365, "price": "799", "name": "Yearly"}
}
