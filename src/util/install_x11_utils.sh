#!/bin/bash

###################
# Install x11 utils #
###################

# Install needed dependencies.
echo "[+] Installing and configuring x11 utils in non-interactive mode...."
sudo apt-get update && apt-get install -y x11-xserver-utils
