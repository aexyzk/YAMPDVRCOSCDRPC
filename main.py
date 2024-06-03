from threading import Thread
from scripts.vrchat import send_vrchat as vrc
from scripts.discord import connect_to_discord as dis
import subprocess, os
import json
import sys

global settings
settings = {
    "MPD Address": "localhost",
    "MPD Port": 6600,
    "VRchat OSC Address": "localhost",
    "VRchat OSC Port": 9000,
}

def save_settings():
    with open('settings.json', 'w') as f:
        json.dump(settings, f)

def load_settings():
    try:
        with open('settings.json', 'r') as f:
            loaded_settings = json.load(f)
            settings.update(loaded_settings)
        print("Loaded Settings Successfully!")
    except FileNotFoundError:
        print("Error: E001: Could not find 'settings.json': Unable to load settings")

load_settings()

def vrchat_thread():
    vrc(settings['VRchat OSC Address'], settings['VRchat OSC Port'], settings['MPD Address'], settings['MPD Port'])

def discord_thread():
    dis(settings['MPD Address'], settings['MPD Port'])

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "--discord":
            print("Starting Discord RPC...")
            discord_thread()
        if sys.argv[1] == "--vrchat":
            print("Starting VRChat OSC...")
            vrchat_thread()
        if sys.argv[1] == "--help":
            print("no args #lauch both vrchat thread and discord thread\n--discord #runs only the discord thread\n--vrchat #runs only the vrchat thread\n--help shows this\nthe config file is located in the same directory 'settings.json'")
    else:
        try:
            print("Starting VRChat OSC, Starting Discord RPC...")
            Thread(target = vrchat_thread).start()
            Thread(target = discord_thread).start()
        except KeyboardInterrupt:
            exit()

if __name__ == "__main__":
    main()

save_settings()