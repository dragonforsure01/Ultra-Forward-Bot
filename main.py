import os
from flask import Flask
from threading import Thread
from bot import Bot

# 1. Setup Flask for Render Health Check
app_web = Flask('')

@app_web.route('/')
def home():
    return "Bot is alive and running!"

def run_web():
    # Render provides a PORT environment variable; we must use it
    port = int(os.environ.get("PORT", 8080))
    app_web.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

# 2. Start the Flask Server
keep_alive()

# 3. Start the Telegram Bot
# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper

print("Starting Bot...")
bot_app = Bot()
bot_app.run()
