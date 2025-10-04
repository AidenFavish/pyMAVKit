#!/bin/bash

cleanup() {
	echo -e "\nCleaning up..."
	pkill mavproxy
	pkill xterm
	pkill 'bash <defunct>'
	pkill python3
	echo -e "\nClean up complete. Exiting..."
}
trap cleanup SIGINT

echo "Starting sim..."
source ~/.bashrc
. ~/.profile

~/forge/ardupilot/Tools/autotest/sim_vehicle.py -v copter --no-mavproxy -w -l 33.7713180251761,-117.69482206241825,0.0,0.0 &

sleep 10

echo 'mavproxy starting'

mavproxy.py --master=tcp:127.0.0.1:5760 --map --console --out=127.0.0.1:14550
