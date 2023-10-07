# accesspoint

[this tutorial]: https://www.raspberrypi.com/documentation/computers/configuration.html#before-you-begin

Setup an access point on a Raspberry Pi using only the necessary packages. Previous projects used Hydrosys to achieve this so I built this to make it easier.

> This code was based on [this tutorial]

### Usage
0. Flash `Raspbian Lite (32-bit)` with Raspberry Pi Imager. When flashing, set the hostname to `raspberrypi` and the wifi to your phone's hostspot (we'll need this internet connection later). 
> Warning! If you already have another Pi or computer with the `raspberrypi` hostname on the network, ssh may introduce some difficulties. Use a different hostname and use that one instead for steps 1 and 3.
1. Once you boot up the Pi, connect your computer to your phone hostspot. Then, `ssh` into it with the following command:
```bash
ssh pi@raspberrypi.local
```
2. Open a new terminal. At this point, you should have 2 terminals: one `ssh`ed into the Pi and one `cd`ed into the `tools` directory of this repo (in your clone of course).
3. Transfer the files `ap.py`, `setup.py`, and `install.sh` to the Pi with `scp`:
```bash
scp ap.py setup.py install.sh pi@raspberrypi.local:/home/pi
```
4. Go to the `ssh` terminal and make sure you are in the home directory (`/home/pi`) with the `pwd` command. Then run the following commands in order:
```bash
sudo bash install.sh
sudo python3 setup.py
```

5. `sudo reboot now` to restart the computer and initialize the access point.

6. After the Pi boots, your computer should list a new network. Connect to it with the credentials from step 4. Then, `ssh` into it with the same process as step 1.

#### Bonus:
- The setup does not require a phone hotspot in paticular. A standard home wifi can be used (and was used for testing) but this is not always available and so the hotspot is a replacement. Not much difference other than network speed (this may affect `install.sh`).
- You can toggle the access point with `sudo python3 ap.py on|off`
- You can change the hostname by editing the `/etc/hostname` file.
- You can change the network number by runing `setup.py` again. It is designed to not double up on it's previous setup.
- If the hostname doesn't seem to be working, try the following:
    - wait a maximum of 5 minutes to allow the Pi to boot up (it may just be slow)
    - Make sure the you are on the same network as the one you specified in step 0. run `arp -a` on your computer while NOT `ssh`ed into the terminal. Then try `ssh pi@[ip]` with every ip address listed.

### Technologies & Scripts
- `hostapd` & `dnsmasq`: These packages are installable through `apt` and are system deamons related to the access point.
- `install.sh`: Updates the Pi, installs necessary libraries/packages, enables `hostapd` and prepares for the Python script.