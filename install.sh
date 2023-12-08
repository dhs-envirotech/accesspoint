#/bin/bash

# The usual
sudo apt update
sudo apt -y upgrade

# Install packages
sudo apt install hostapd dnsmasq
sudo DEBIAN_FRONTEND=noninteractive apt install -y netfilter-persistent iptables-persistent

# Enable hostapd
sudo systemctl unmask hostapd
sudo systemctl enable hostapd

# Prepare for python script
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig

# The tutorial says so...
sudo rfkill unblock wlan