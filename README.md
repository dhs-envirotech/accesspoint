# accesspoint

[this tutorial]: https://www.raspberrypi.com/documentation/computers/configuration.html#before-you-begin

Setup an access point on a Raspberry Pi using only the necessary packages. Previous projects used Hydrosys to achieve this so I built this to make it easier.

> This code was based on [this tutorial]

### Usage
0. [Setup the Pi](https://github.com/orgs/dhs-envirotech/discussions/6)
1. `ssh` into the Pi
2. Clone the repo:
```bash
git clone https://github.com/dhs-envirotech/accesspoint.git
```
3. Install the software necessary
```bash
sudo bash install.sh
```
4. Configure
> This setup script always sets the password to the lowercase version of the provided SSID. Spaces & dashes will be removed from the password

Make sure to note down the credentials the script spits out at the end.
```bash
sudo python3 configure.py
```
5. `sudo reboot now` to restart the computer and initialize the access point.
6. After the Pi boots, your computer should list a new network. Connect to it with the credentials from step 5. Then, `ssh` into it.

### Other notes:
- You can toggle the access point with `sudo python3 ap.py on|off`
- You can reconfigure by just running the script again. It will overwrite changes.

### Technologies & Scripts
- `hostapd` & `dnsmasq`: These packages are installable through `apt` and are system daemons related to the access point.
- `install.sh`: Updates the Pi, installs necessary libraries/packages, enables `hostapd`, and prepares for the Python script.
