# Yet Another MPD VRChat OSC Discord RPC Status thingy

## Running
1. Install Python
2. Decompress the .zip
3. Install dependencies 'deps.txt' using pip
4. Use a Terminal (Alacritty, Konsole, Powershell, etc), to navigate to the main folder.
5. Run `python3 main.py` to open the python file.
6. Go to 'mpd-osc-rpc.json' (this will be in the same folder as the script if you run the program once, on windows, on linux its in ~/.config/mpd-osc-rpc.json) and setup all addresses and ports this is default, perfect if you are running VRChat and MPD on the same computer, but for standalone VRChat or more complicated MPD setups you may have to change these in the config file
```
    "MPD Address": "localhost",
    "MPD Port": 6600,
    "VRchat OSC Address": "localhost",
    "VRchat OSC Port": 9000,
```
7. Then you can run it :]
   - (for Linux i recommend having it startup with MPD, as it's finally reliable enough to run without crashing)
   - (i don't know how to make stuff start by default on windows)
8. Arguments
```
  no args #lauch both vrchat thread and discord thread
  --discord #runs only the discord thread
  --vrchat #runs only the vrchat thread
  --help #this shows info
```
---

## Required For Discord (if you wanna rename the RPC)
1. Go to Discord Dev Hub https://discord.com/developers/applications
2. Create a new app
3. Copy the Client ID
4. Go to "Settings"
5. Set your Discord RPC ID to the one you just copied

---

## (if you run into any bugs you can report them on github or feel free to contact me here https://aexyzk.github.io/#contact)
