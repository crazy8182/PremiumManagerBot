import os

API_ID = int(os.environ.get("API_ID", "26741021"))
API_HASH = os.environ.get("API_HASH", "7c5af0b88c33d2f5cce8df5d82eb2a94")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8767741403:AAGQcNQrcVtwuKACMFBpw6eKBRp4MKloH3c")

MONGO_URI = os.environ.get("MONGO_URI", "mongodb+srv://devashibambhava0:devashibambhava0@cluster0.ux6amy9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

ADMIN_ID = [6859451629]

PREMIUM_GROUP_ID = -1003349439139
LOG_CHANNEL = -1003527401159

UPI_ID = "BHARATPE09917731344@yesbankltd"

QR_IMAGE = "https://ibb.co/9k9QT8sg"

PLANS = {
    "1month": {"days": 30, "price": "69", "name": "Monthly"},
    "3month": {"days": 90, "price": "179", "name": "Quarterly"},
    "6month": {"days": 180, "price": "299", "name": "Haf-Yearly"},
    "12month": {"days": 365, "price": "549", "name": "Yearly"}
}
