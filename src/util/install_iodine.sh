#!/bin/bash

###################
# Install Iodine  #
###################

# Install needed dependencies.
sudo apt-get update && apt-get install -y git check make pkg-config gcc

# CLone the repo
git clone https://github.com/yarrick/iodine.git
cd iodine

# Lets build it 
make 
sudo make install 

# Check tests 
make test