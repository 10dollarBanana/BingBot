#! /bin/bash

# Create xauth file, if missing
#/bin/bash -c 'ln -s "$AUTHORITY" ~/.Xauthority'

# Create python virtual environment
# python -m venv env/

# Navigate and update
cd /home/jason/BingBot
git fetch 
git reset --hard HEAD
git merge '@{u}'

# Make executable
cd /home/jason/BingBot/VM
chmod 777 *.py
chmod 777 *.sh

# Random sleep
low=10
hgh=1800
rand=$((low + RANDOM%(1+hgh-low)))
sleep $rand

# touch test.txt

# source env/bin/activate
# XAUTHORITY=home/<user ./.Xauthority

# Queue Bing search
DISPLAY=:0 python3 Bing.py

#python3 BingBot.py

# Queue Bing Shopping
# until [ -f search.complete ]
# do
#      sleep 5
# done

# rm search.complete
# DISPLAY=:0 python3 BingShopping.py


# Queue Bing Workout
# until [ -f search.complete ]
# do
#     sleep 5
# done

rm search.complete
# DISPLAY=:0 python3 BingWorkout.py

