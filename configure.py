import os
import sys
import re

if 'SUDO_UID' not in os.environ.keys():
    print('Run this script with sudo!')
    exit(1)

# Get input

# MODIFIED SCRIPT FOR GROWBOX
# print('This script has been modified for the Growbox project')
# n = input('Number> ')
# int(n)
# ssid = 'ES Growbox ' + n
# password = 'esgrowbox' + n
# hostname = 'raspberrypi' + n

ssid = input("SSID: ")
password = input("Password: ").replace('-', '').replace(' ', '').lower()

hostname = input(f"Hostname: ")
if ' ' in hostname:
    print("\nPlease do not use spaces in the hostname")
    exit(1)

# File Contents
dhcpcd="""# ap-block-start
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
# ap-block-end"""
hostapd="""country_code=GB
interface=wlan0
ssid=SSID
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=PASSWORD
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
"""
dnsmasq="""interface=wlan0 # Listening interface
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
                # Pool of IP addresses served via DHCP
domain=wlan     # Local wireless DNS domain
address=/router.wlan/192.168.4.1
                # Alias for this router
"""

dhcpcd_path="/etc/dhcpcd.conf"
with open(dhcpcd_path, "r") as r:
    s = r.read()
    if 'nohook' not in s:
        with open(dhcpcd_path, "a") as w:
            w.write(dhcpcd)

with open("/etc/hostapd/hostapd.conf", "w") as file:
    file.write(hostapd.replace('SSID', ssid).replace('PASSWORD', password))

with open("/etc/dnsmasq.conf", "w") as file:
    file.write(dnsmasq)

hosts = "/etc/hosts"
with open(hosts, 'r') as file:
    text = file.read()
    terms = re.findall(r'[a-zA-Z0-9\-.:]+', text)

with open(hosts, 'w') as file:
    file.write(text.replace(terms[-1], hostname))

os.system('sudo hostnamectl set-hostname ' + hostname)

print(r"""Setup completed! Re-run for new settings.

{YELLOW}SSID:{YELLOW}     {GREEN}{ssid}{RESET}
{YELLOW}PASSWORD:{YELLOW} {GREEN}{password}{RESET}
{YELLOW}HOSTNAME:{YELLOW} {GREEN}{hostname}{RESET}

⚠️  Please reboot to enable all services. Please note your wifi ssid and password as 
   your SSH connection will be lost and this access point should start its own.""".format(
    YELLOW=sys.stderr.isatty() and "\033[33m" or "",
    GREEN=sys.stderr.isatty() and "\033[32m" or "",
    RESET=sys.stderr.isatty() and "\033[0m" or "",
    ssid=ssid,
    password=password,
    hostname=hostname
))