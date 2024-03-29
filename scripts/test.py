from discordrp import Presence
import time

client_id = "1223344645908729867"  # Replace this with your own client id

with Presence(client_id) as presence:
    print("Connected")

    while True:
        presence.set(
            {
                "state": "In Game",
                "details": "Summoner's Rift",
                "timestamps": {"start": int(time.time())},
            }
        )
        print("Presence updated")
        time.sleep(15)