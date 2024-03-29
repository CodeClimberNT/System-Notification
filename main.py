import os
import asyncio
import socket
from datetime import datetime
from dotenv import load_dotenv
from telegram import Bot

# Load environment variables from .env file
load_dotenv()

# Get Telegram bot token and chat ID from environment variables
bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

async def send_telegram_message(message):
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)

def main():
    # Get the current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the computer name
    computer_name = socket.gethostname()
    
    # Create the message with date, time, and computer name
    message = f"Your computer '{computer_name}' has been powered on at {current_time}."
    
    # Send the message
    asyncio.run(send_telegram_message(message))

if __name__ == "__main__":
    main()
