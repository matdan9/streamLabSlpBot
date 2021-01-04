#!/bin/bash

pip3 install "python-socketio[client]"
pip3 install RPi.GPIO
sudo cp ./slapBot/slpConfig.json /etc
sudo cp -r slapBot /usr/bin
sudo cp slp /usr/bin
sudo chmod +x /usr/bin/slp
