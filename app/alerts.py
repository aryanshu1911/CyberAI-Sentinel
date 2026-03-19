import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_alert(message: str):
    """
    Send a Telegram alert using bot token and chat ID from .env
    """
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print(f"📨 Alert sent: {message}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Failed to send alert: {e}")