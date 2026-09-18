from flask import Flask
import threading
import os
import time

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_bot():
    print("Bot started...")
    while True:
        # هنا كود التداول ديالك (تقدر تبدلو من بعد)
        print("Checking market...")
        time.sleep(60)

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
