NOTE: This is an update to the accesspoint instructions below (Starting at "# accesspoint"
1) Hotspot support is now part of Raspbien, can can be controlled through the graphical desktop, or the command line using "nmcli".
2) Useful nmcli commands are as follows:
   a) sudo nmcli device wifi hotspot ssid <YOURSSID> password <YOURPWD>
      (Note: above will create a hotspot - YOURPWD MUST BE >=7 characters
   b)  nmcli connection show --active
       (Note: above will show active connections.  Use this to find the UUID of the preconfigured wireless network that you may use by default.  You will need this to
        switch back fromm a hotspot to the preconfigured, shared network.  EX:

         nmcli connection show --active 
         NAME           UUID                                  TYPE      DEVICE 
         preconfigured  d26740e1-5c55-4677-b5ec-b3f7b9dcbd93  wifi      wl

         Use the same nmcli connection show --active  command to obtain the hotspot UUID once connected and logged in over the hotspot.

       You can put the above into a script to switch back from the hotspot to the default shared network

         sudo nmcli con down 43d97f0f-1351-4122-a040-9ee87ef26a27
         sudo snmcli con up d26740e1-5c55-4677-b5ec-b3f7b9dcbd93

      c)  nmcli c
          The above will show a history of connections

      USING The above information, you should be able to write a script that is called during system startup, usually as a script in /etc/init.d, and then symlinnked with
      an appropriate name in /etc/rc3.d (this is where networking is turned on.  You could call it SNhotspot, where "N" is a number signifying where in the order you want
      to start it.

       See: https://www.novell.com/documentation/suse91/suselinux-adminguide/html/ch13s04.html

   NOTES BELOW ARE ORIGINAL INSTRUCTIONS FOR HOTSPOTS


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
