import sys, os

if 'SUDO_UID' not in os.environ.keys():
    print('Run this script with sudo!')
    exit(1)

# Config
mode = sys.argv[1]
path = "/etc/dhcpcd.conf"

start_keyword = "ap-block-start"
end_keyword = "ap-block-end"
comment_prefix = "# "

# Check mode
apOff= False
if mode == "on":
    apOff = False
    os.system("sudo systemctl enable hostapd dnsmasq")
elif mode == "off":
    apOff = True
    os.system("sudo systemctl disable hostapd dnsmasq")
else:
    print("Invalid mode " + mode + ": Please choose 'on' or 'off'")
    sys.exit(1)

# Read All Lines
with open(path, 'r') as file:
    lines = file.readlines()

# Open For Writing
with open(path, 'w') as file:
    found_start = False

    for line in lines:
        if start_keyword in line:
            found_start = True
            file.write(line)
            continue
        elif end_keyword in line:
            found_start = False
            file.write(line)
            continue

        if found_start:
            if apOff and not line.startswith(comment_prefix):
                file.write(comment_prefix + line)  # Add prefix
                continue
            elif not apOff and line.startswith(comment_prefix):
                file.write(line[len(comment_prefix):])  # Remove prefix
                continue
        
        file.write(line)

if not apOff:
    yes = input('Turn on now (yes/no)?\n> ')
    if yes == 'yes':
        os.system('bash /home/pi/accesspoint/on.sh &')