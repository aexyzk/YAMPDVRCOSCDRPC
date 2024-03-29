from pythonosc.udp_client import SimpleUDPClient
from pythonosc import udp_client
import time
import os

from scripts.music import get_music

osc_message = ["", True]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_message(msg):
    osc_message[0] = msg
    client.send_message("/chatbox/input",osc_message)
    print("Sent messange to VRChat!")

def send_vrchat(address, port, mpd_address, mpd_port):
    global client
    client = SimpleUDPClient(address, port)

    while True:
        clear()
        output = ''
        music = get_music(mpd_address, mpd_port)

        print(music)

        if music[3] != '':
            output = music[3]
        else:
            output = f"{music[2]} {music[0]} - {music[1]}"

        send_message(output)
        time.sleep(2)