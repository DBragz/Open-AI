#!/usr/local/bin/python3

"""
    Prints all available wi-fi networks. In order to get the program to work on
    a Mac you must run the following commands.
    1. python3 -m pip uninstall pywifi
    2. git clone -b macos_dev https://github.com/awkman/pywifi
    3. cd pywifi
    4. pip3 install .
    Author: Daniel Ribeirinha-Braga
"""

# Print all available wi-fi networks
import pywifi

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]
iface.scan()

print("Available networks:")

for network in iface.scan_results():
    print(network.ssid)
