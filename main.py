import os
import time
from flask import Flask
from threading import Thread
from bot import Bot

# 1. Setup Flask
app_web = Flask(__name__)

@app_web.route('/')
def home():
    return "Bot is alive!"

def run_web():
    # Render assigns a port dynamically. We MUST use os.environ.get('PORT')
    port = int(os.environ.get("PORT", 8080))
    print(f"--- Flask is starting on port {port} ---")
    app_web.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run_web)
    t.daemon = True
    t.start()

# 2. Start Flask FIRST
if __name__ == "__main__":
    keep_alive()
    
    # Give Flask 2 seconds to bind to the port before starting the bot
    time.sleep(2) 
    
    print("--- Starting Telegram Bot ---")
    # Jishu Developer Credits
    bot_app = Bot()
    bot_app.run()
