#!/bin/bash

###################
# Install Wireshark #
###################

# Install needed dependencies.
echo "[+] Installing Wireshark in non-interactive mode...."
sudo apt-get update
echo "wireshark-common wireshark-common/install-setuid boolean true" | sudo debconf-set-selections
sudo DEBIAN_FRONTEND=noninteractive apt-get -y install wireshark