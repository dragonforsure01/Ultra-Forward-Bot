import os
import threading
from flask import Flask
from bot import Bot

# 1. Setup the Web Server
app_web = Flask(__name__)

@app_web.route('/')
def health_check():
    return "Bot is running!", 200

def start_bot():
    print("--- Starting Telegram Bot ---")
    try:
        # Credits: JishuDeveloper
        bot_app = Bot()
        bot_app.run()
    except Exception as e:
        print(f"Bot Error: {e}")

# 2. Main Execution
if __name__ == "__main__":
    # Start the bot in a separate background thread
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.daemon = True
    bot_thread.start()

    # Start the Web Server (This keeps Render happy and shows 'Live')
    port = int(os.environ.get("PORT", 8080))
    print(f"--- Web Server starting on port {port} ---")
    app_web.run(host='0.0.0.0', port=port)
