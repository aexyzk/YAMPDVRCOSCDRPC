# YetAnotherMusicPlayerDaemonVRChatOpenSoundControlDiscordRichPresenceClient

## Using Precompiled binary
1. Download from releases tab
2. Unzip it
3. Double click it!
 - (If you're on linux run 'chmod +x main' while in the folder)
 - (If you're on windows, windows defender might see it as a virus, this is a bug with pyinstaller)
4. Go to settings and setup all addresses and ports this is default, perfect if you are running VRchat and MPD on the same computer, but for standalone VRChat or more complicated MPD setups you may have to change these in the settings
```
settings = {
    "DiscordID": "",
    "MPD Address": "localhost",
    "MPD Port": 6600,
    "VRchat OSC Address": "localhost",
    "VRchat OSC Port": 9000,
}
```
5. Then you can run it :]

---

## Reqired For Discord)
1. Go to Discord Dev Hub https://discord.com/developers/applications
2. Create a new app
3. Copy the Client ID
4. Go to "Settings"
5. Set your Discord RPC ID to the one you just copied

## (Running from source)
1. Install Python (I used 3.11)
2. Decompress the .zip
3. Use a Terminal (Powershell, Alacritty, Konsole, etc), to navigate to the main folder.
4. Run `python3 ./main.py` to open the python file.

### (You can change your addresses for MPD and OSC (for quest or any other standalone vrchat) in the settings)

Then you're all good

(if you run into any bugs you can report them on github or contact me here https://aexyzk.github.io/contact)
