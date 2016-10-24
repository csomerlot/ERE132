# ERE132

## Setup of RPi from stock raspbian-lite:
- start disconnected from network
- Change keyboard: sudo nano /etc/default/keyboard so that XKBLAYOUT="us"
-- or: L='us' && sudo sed -i 's/XKBLAYOUT=\"\w*"/XKBLAYOUT=\"'$L'\"/g' /etc/default/keyboard
- Change hostname from default raspberrypi via: sudo nano /etc/hostname
- plug into network
- sudo reboot now
- install WebIDE via: curl https://raw.githubusercontent.com/adafruit/Adafruit-WebIDE/alpha/scripts/install.sh | sudo sh -s - --offline
- sudo apt-get install python-pip
- sudo pip install adafruit-mcp3008

## from another computer:
- connect to <newhostname>[.esf.edu] from web browser
- The web IDE editor should open and you can clone this repository: https://github.com/csomerlot/ERE132.git
- refresh the project pane and find StudentCode\collectData.py
- change code and RUN

## back on RPi:
- Create a symlink in /etc/init.d: sudo ln -s /home/webide/repositories/ERE132/StudentCode/collectData.py /etc/init.d/collectData
- change creds: sudo chmod a+rwx /home/webide/repositories/ERE132/StudentCode/collectData.py
- set the collectData.py file to be run automatically on boot: sudo update-rc.d collectData defaults
