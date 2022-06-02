#!/bin/bash

###################
# Install Wireshark #
###################

# Install needed dependencies.
echo "[+] Installing and configuring x11 utils in non-interactive mode...."
sudo apt-get update && apt intsall -y x11-xserver-utils
sudo su 
xauth merge ~vagrant/.Xauthority
export DISPLAY=localhost:10.0