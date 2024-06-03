from discordrp import Presence
import time

from scripts.music import get_music

id = "1223344645908729867"

def send_discord(addr, port):
    with Presence(id) as presence:
        print("connected to discord")
        while True:
            music = get_music(addr, port)
            if music[2] != "⏸️" and music[2] != "⏹️" and music[3] == '':
                presence.set(
                    {
                        "details": f"{music[0]}",
                        "state": f"by {music[1]}",
                        "timestamps": {"end": music[5]},
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
        except:
            print('cannot find a vaild discord instance')
        print('failed')
        time.sleep(15)
        print("timer complete")