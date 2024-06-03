# Yet Another MPD VRChat OSC Discord RPC Status thingy

## Using Precompiled binary
1. Download from releases tab
2. Unzip it
3. Run it!
 - (If you're on linux run 'chmod +x main' while in the folder, to allow it to be executable)
 - (If you're on windows, windows defender might see it as a virus)
4. Go to 'settings.json' (this will be in the same folder as the executable if you run the program once) and setup all addresses and ports this is default, perfect if you are running VRChat and MPD on the same computer, but for standalone VRChat or more complicated MPD setups you may have to change these in the config file
```
    "MPD Address": "localhost",
    "MPD Port": 6600,
    "VRchat OSC Address": "localhost",
    "VRchat OSC Port": 9000,
```
5. Then you can run it :]
   - (for Linux i recommend having it startup with MPD, as it's finally reliable enough to run without crashing)
   - (i don't know how to make stuff start by default on windows)

---

## (Running from source)
1. Install Python
2. Decompress the .zip
3. Install dependencies 'deps.txt' using pip
4. Use a Terminal (Alacritty, Konsole, Powershell, etc), to navigate to the main folder.
5. Run `python3 main.py` to open the python file.

## (Building from source)
1. Install Python
2. Decompress the .zip
3. Install dependencies 'deps.txt' and 'pyinstaller' using pip 
4. Use a Terminal (Alacritty, Konsole, Powershell, etc), to navigate to the main folder.
5. Run `pyinstaller main.py --onefile` to open the python file.

## Reqired For Discord (If running from source)
1. Go to Discord Dev Hub https://discord.com/developers/applications
2. Create a new app
3. Copy the Client ID
4. Go to "Settings"
5. Set your Discord RPC ID to the one you just copied

### this is the same for every platform however the command for python and pip could be diffrent
```
  py
  python
  python3

  pip
  python3 -m pip
  py -m pip
  python -m pip
```

---

## (if you run into any bugs you can report them on github or feel free to contact me here https://aexyzk.github.io/#contact)
