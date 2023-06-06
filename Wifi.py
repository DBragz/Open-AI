

import wifi

def find_wifi_networks():
  # Get a list of available Wi-Fi networks
  networks = wifi.Cell.all('wlan0')
                
  wifi_networks = []
                     
  # Iterate over the available networks
  for network in networks:
    ssid = network.ssid
    signal = network.signal
                                                            
    # Append the network information to the list
    wifi_networks.append({
      'ssid': ssid,
      'signal_strength': signal
    })
  return wifi_networks

                                                # Call the function to find and print the Wi-Fi networks
wifi_networks = find_wifi_networks()

for network in wifi_networks:
  print(f"SSID: {network['ssid']}")
  print(f"Signal Strength: {network['signal_strength']} dBm")

