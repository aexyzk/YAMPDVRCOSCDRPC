from discordrp import Presence
import time

from scripts.music import get_music

def send_discord(id, addr, port):
    with Presence(id) as presence:
        print("Connected")

        while True:
            music = get_music(addr, port)

            if music[3] == '':
                if music[2] == "⏸️":
                    presence.set(
                        {
                            "details": "Nothing is playing",
                            "state": ":3",
                        }
                    )
                else:
                    presence.set(
                        {
                            "details": f"{music[0]}",
                            "state": f"by {music[1]}",
                        }
                    )
            else:
                presence.set(
                    {
                        "details": f"{music[3]}",
                        "state": ":3",
                    }
                )
            print("Sent message to Discord")
            time.sleep(15)