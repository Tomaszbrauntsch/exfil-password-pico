# Instructions
1. Install [Thonny] Python IDE (https://thonny.org/) (straight forward installation)
2. Download the (CircuitPython UF2 file)[https://circuitpython.org/board/raspberry_pi_pico/], once downloaded, press and hold the BOOTSEL button while connecting the pico. After the pico is connected, the storage folder should pop up then drag and drop the CircuitPython UF2 into that folder. When the UF2 file transfer is complete the folder will close out and the pico will reboot.
3. Download the 9.x release from the (Adafruit Circuit Python Github) [https://github.com/adafruit/Adafruit_CircuitPython_HID], extract the .zip file, open the extracted files and navigate to the lib folder. Once in the lib folder, transfer the *adafruit_hid* folder into the lib folder of the pico.

The program autoruns when plugged in, so make sure the BOOTSEL button is held down while plugged in to analyze the code of the chip and not accidently running the program 
