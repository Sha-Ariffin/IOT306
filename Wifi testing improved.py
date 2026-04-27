import network

# Create WLAN interface (station mode)
wlan = network.WLAN(network.STA_IF)

# Activate the interface
wlan.active(True)

# Scan for nearby networks
networks = wlan.scan()

# Print results
for net in networks:
    ssid = net[0].decode('utf-8')
    bssid = net[1]
    channel = net[2]
    rssi = net[3]
    security = net[4]
    hidden = net[5]

    print("SSID:", ssid)
    print("RSSI (Signal Strength):", rssi)
    print("Channel:", channel)
    print("Security:", security)
    print("---------------------------")