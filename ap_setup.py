import network
import time
import socket

# setup flask
def web_page():
  html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
            <body><h1>Hello World</h1></body></html>
         """
  fileContents = ""
  html += fileContents
  # reads the file and appends to the html file
  return html

# if you do not see the network you may have to power cycle
# unplug your pico w for 10 seconds and plug it in again
def ap_setup(ssid, password):
    """
        Description: This is a function to activate AP mode

        Parameters:

        ssid[str]: The name of your internet connection
        password[str]: Password for your internet connection

        Returns: None
    """
    # Just making our internet connection
    ap = network.WLAN(network.AP_IF) # future TOOD: don't broadcast network, if possible
    ap.config(essid=ssid, password=password)
    ap.active(True)

    while ap.active() == True:
        print('AP Mode is accepting connections')
        print('IP Address: ' + ap.ifconfig()[0])

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
        s.bind(('', 80)) # random ip address
        s.listen(5)

        while True: # accept connections
          conn, addr = s.accept()
          print('Got a connection from %s' % str(addr))
          request = conn.recv(1024) # future TODO: check for specific useragent
          print('Content = %s' % str(request))
          response = web_page()
          conn.send(response)
          conn.close()

def main():
    # autorun configuration
        # emulate keyboard and save to results to the pico
    # run the script for autorun
    ap_setup('NAME_STR', 'PASSWORD_STR') # sets up the website and the information