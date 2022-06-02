#!/bin/bash

cp /home/vagrant/.Xauthority /root/.Xauthority
xauth merge /home/vagrant/.Xauthority
export DISPLAY=localhost:10.0
