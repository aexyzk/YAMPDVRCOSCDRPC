from pythonosc.udp_client import SimpleUDPClient
from pythonosc import udp_client
from datetime import datetime
import time

from scripts.music import get_music

osc_message = ["", True]

def send_message(msg):
    osc_message[0] = msg
    client.send_message("/chatbox/input",osc_message)
    print(osc_message)

def send_vrchat(address, port, mpd_address, mpd_port):
    global client
    client = SimpleUDPClient(address, port)

    while True:
        output = ''
        music = get_music(mpd_address, mpd_port)

        print(music)

        cur_time = datetime.now().strftime('%H:%M')
        if music[3] != '':
            output = str(cur_time)
        else:
            output = f"{music[2]} {music[1]} - {music[0]} {datetime.utcfromtimestamp(int(music[6])).strftime('%M:%S')} left | {cur_time}"

        send_message(output)
        time.sleep(2)