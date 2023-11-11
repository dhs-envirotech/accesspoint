# accesspoint

[this tutorial]: https://www.raspberrypi.com/documentation/computers/configuration.html#before-you-begin

Setup an access point on a Raspberry Pi using only the necessary packages. Previous projects used Hydrosys to achieve this so I built this to make it easier.

> This code was based on [this tutorial]

### Usage
0. [Setup the Pi](https://github.com/orgs/dhs-envirotech/discussions/6)

Please use `Raspberry Pi OS Lite LEGACY 32-bit`
1. Once you boot up the Pi, connect your computer to your phone hostspot. Then, `ssh` into it with the following command:
```bash
ssh pi@raspberrypi.local
```
2. Open a new terminal. At this point, you should have 2 terminals: one `ssh`ed into the Pi and one `cd`ed into the `tools` directory of this repo (in your clone of course).
3. Transfer the files `ap.py`, `setup.py`, and `install.sh` to the Pi with `scp`:
```bash
scp ap.py setup.py install.sh pi@raspberrypi.local:/home/pi/accesspoint
```
4. Install the software necessary:
```bash
sudo bash install.sh
```
5. Go to the `ssh` terminal and make sure you are in the `accesspoint` directory (`/home/pi/accesspoint`) with the `pwd` command. 
> This setup script always sets the password to the lowercase version of the provided SSID. Spaces are not allowed & dashes will be removed from the password

Make sure to note down the credentials the scripts spits out at the end.
```bash
sudo python3 setup.py
```
6. `sudo reboot now` to restart the computer and initialize the access point.
7. After the Pi boots, your computer should list a new network. Connect to it with the credentials from step 5. Then, `ssh` into it with the same process as step 1.

### Other notes:
- You can toggle the access point with `sudo python3 ap.py on|off`
- You can change the network number by runing `setup.py` again. It is designed to not double up on its previous setup.

### Technologies & Scripts
- `hostapd` & `dnsmasq`: These packages are installable through `apt` and are system deamons related to the access point.
- `install.sh`: Updates the Pi, installs necessary libraries/packages, enables `hostapd` and prepares for the Python script.