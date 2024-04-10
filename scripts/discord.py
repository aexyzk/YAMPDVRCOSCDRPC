from discordrp import Presence
import time

from scripts.image_collector import find_image
from scripts.music import get_music

#id = "SET YOUR DISCORD APPLICATION ID HERE"
id = "1223344645908729867"
# https://discord.com/developers/applications

def send_discord(addr, port):
    #while True:

        #if music[2] != "⏸️":
            with Presence(id) as presence:
                print("Connected")

                while True:
                    music = get_music(addr, port)
                    try:
                        query = (f"{music[4]} - {music[1]} cover")
                        tooltip = music[4]
                    except:
                        query = (f"{music[0]} - {music[1]} cover")
                        tooltip = music[0]
                    album_cover = find_image(query)
                    if music[2] != "⏸️" and music[3] == '':
                        presence.set(
                            {
                                "details": f"{music[0]}",
                                "state": f"by {music[1]}",
                                "assets": {
                                    "large_image": album_cover,  # Replace this with the key of one of your assets
                                    "large_text": f"{tooltip} (This cover art may not be correct)",
                                    "small_image": "https://www.musicpd.org/logo.png",  # Replace this with the key of one of your assets
                                    "small_text": "MPD Logo",
                                },
                            }
                        )
                    else:
                        presence.clear()
                        print("breaked")
                    print("Sent message to Discord")
                    time.sleep(15)