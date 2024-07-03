from discordrp import Presence
import time

from scripts.music import get_music
from scripts.get_art import *

id = "1223344645908729867"

def send_discord(addr, port):
    with Presence(id) as presence:
        print("connected to discord")
        _cover = cover()
        while True:
            music = get_music(addr, port)
            if music[2] != "⏸️" and music[2] != "⏹️" and music[3] == '':
                print(music)
                artist = music[1].split("/")[0].strip()
                if music[4] is None:
                    search = f"{music[0]} - {artist}"
                else:
                    # fix self titled albums breaking
                    if music[1] != music[4]:
                        search = f"{music[4]} - {artist}"
                    else:
                        search = f"{music[0]} - {artist}"
                presence.set(
                    {
                        "details": f"{music[0]}",
                        "state": f"by {music[1]}",
                        "timestamps": {"end": music[5]},
                        "assets": {
                            "large_image": _cover.get_cover(search),
                            "large_text": search,
                        },
                    }
                )
                print(f"details: {music[0]}", f"state: by {music[1]}", f"timestamps: end: {music[5]}")
            else:
                print(f"cleared presence")
                presence.clear()
            time.sleep(15)

def connect_to_discord(addr, port):
    while True:
        print('trying to conect to discord')
        try:
            send_discord(addr, port)
        except ConnectionRefusedError:
            print('cannot find a vaild discord instance')
        except Exception as e:
            print(e)
        print('failed')
        time.sleep(15)
        print("timer complete")