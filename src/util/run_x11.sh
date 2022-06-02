#!/bin/bash

sudo su
xauth merge /home/vagrant/.Xauthority
export DISPLAY=localhost:10.0
exit