from mpd import MPDClient

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
                artist = song.get('artist', '')
                title = song.get('title', '')
                toggle ="⏸️"
            else:
                artist = song.get('artist', '')
                title = song.get('title', '')
                toggle = f"▶️"
        else:
            return ('', '', '', "No songs in queue")
            
    except ConnectionError:
        return ('', '', '', "MPD Offline")

    return (title, artist, toggle, err)