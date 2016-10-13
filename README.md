# ERE132

## Setup of RPi from stock raspbian-lite:
- start disconnected from network
- sudo raspi-config to internationalisation options to change keyboard layout to English (US)
- Change hostname from default raspberrypi via: sudo nano /etc/hostname
- plug into network
- sudo reboot now
- install WebIDE via: curl https://raw.githubusercontent.com/adafruit/Adafruit-WebIDE/alpha/scripts/install.sh | sudo sh -s - --offline
- sudo apt-get install build-essential python-dev python-smbus git
- git clone https://github.com/adafruit/Adafruit_Python_MCP3008.git
- cd Adafruit_Python_MCP3008
- sudo python setup.py install

## from another computer:
- connect to <newhostname>[.esf.edu] from web browser
- The web IDE editor should open and you can clone this repository: https://github.com/csomerlot/ERE132.git
- refresh the project pane and find StudentCode\collectData.py
- change code and RUN

## back on RPi:
- Create a symlink in /etc/init.d: sudo ln -s /home/webide/repositories/ERE132/StudentCode/collectData.py 
- change creds: sudo chmod a+rwx /home/webide/repositories/ERE132/StudentCode/collectData.py
- set the collectData.py file to be run automatically on boot: sudo update-rc.d collectData defaults