import sys

ssid = input("SSID (e.g. RaspberryPi3)\n> ")
if ' ' in network_name:
    print("\nPlease do not use spaces in the ssid.")
    exit(1)
password = ssid.lower()

# File Contents
dhcpcd=f"""# ap-block-start
interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
# ap-block-end"""
hostapd="""country_code=GB
interface=wlan0
ssid={ssid}
hw_mode=g
channel=7
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase={password}
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
"""
dnsmasq="""interface=wlan0 # Listening interface
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
                # Pool of IP addresses served via DHCP
domain=wlan     # Local wireless DNS domain
address=/gw.wlan/192.168.4.1
                # Alias for this router
"""

dhcpcd_path="/etc/dhcpcd.conf"
with open(dhcpcd_path, "r") as r:
    s = r.read()
    if 'nohook' not in s:
        with open(dhcpcd_path, "a") as w:
            w.write(dhcpcd)

with open("/etc/hostapd/hostapd.conf", "w") as file:
    file.write(hostapd)

with open("/etc/dnsmasq.conf", "w") as file:
    file.write(dnsmasq)

print(r"""Setup completed!

{YELLOW}SSID:{YELLOW}     {GREEN}{ssid}{RESET}
{YELLOW}PASSWORD:{YELLOW} {GREEN}{password}{RESET}

⚠️  Please reboot to enable all services. Please note your wifi ssid and password as 
   your SSH connection will be lost and this access point should start its own.""".format(
    YELLOW=sys.stderr.isatty() and "\033[33m" or "",
    GREEN=sys.stderr.isatty() and "\033[32m" or "",
    RESET=sys.stderr.isatty() and "\033[0m" or "",
    ssid=ssid,
    password=password,
))