import network
wlan=network.WLAN(network.STA_IF)
if wlan.isconnected():
    wlan.disconnect()
wlan.active(False)
