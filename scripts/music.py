from mpd import MPDClient
import time

def get_music(addr, port):
    err = ''

    try:
        client = MPDClient()

        client.connect(addr, port)
        client.update()
        
        status = client.status()
        song = client.currentsong()

        if bool(song):
            if status["state"] == "pause":
                toggle ="⏸️"
            elif status["state"] == "stop":
                toggle = "⏹️"
            else:
                toggle = f"▶️"

            artist = song.get('artist', '')
            title = song.get('title', '')
            album = song.get('album', '')

            duration_seconds = float(status['duration'])
            elapsed_seconds = float(status['elapsed'])
            time_left_unix_time = int(time.time()) + int(duration_seconds - elapsed_seconds)
        else:
            return ('', '', '', "No songs in queue")
            
    except ConnectionError:
        return ('', '', '', "MPD Offline")

    return (title, artist, toggle, err, album, time_left_unix_time, int(duration_seconds - elapsed_seconds))