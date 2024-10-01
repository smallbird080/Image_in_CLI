#!/bin/bash

mkdir output
chmod +x print.sh showimg.py

sudo apt-get update
sudo apt-get install -y libgl1-mesa-glx 

pip install numpy opencv-python argparse

cd ..
sudo mv ./Image_in_CLI /usr/local/bin/Image_in_CLI
sudo ln -s /usr/local/bin/Image_in_CLI/showimg.py /usr/local/bin/showimg