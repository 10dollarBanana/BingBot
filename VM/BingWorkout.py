#!/usr/bin/python3

import pandas
import pyautogui
import time
import webbrowser
import random
from datetime import date

config="about:config"
type_int=0.2

EDGE_USER_AGENT = ('Mozilla/5.0'
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/114.0.0.0 Safari/537.36 Edge/114.0.1823.58')

def user_agent_switcher(user_agent):
    b = webbrowser.get('firefox')
    b.open_new_tab(config)
    time.sleep(2)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.typewrite("general.useragent.override", interval=0.01)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('right')
    pyautogui.hotkey('right')
    time.sleep(1)
    pyautogui.hotkey('enter')
    pyautogui.typewrite(user_agent, interval=0.01)
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'q')

# Read in csv
df = pandas.read_csv('workoutLinks.csv')

# Get todays date
today = date.today()
day = today.day

# Filter day, get urls
df2 = df.query('Day==@day')
col_list = df2["URL"].values.tolist()
waitTime = df2["Time"].values.tolist()

time.sleep(3)
user_agent_switcher(EDGE_USER_AGENT)
time.sleep(3)

sleep = random.randint(0,300)
time.sleep(sleep)

# Edge
for i in range(2):
    count = i + 1
    url = col_list[i]
    sleep = waitTime[i] + 90
    b = webbrowser.get('firefox')
    b.open_new_tab(url)
    time.sleep(sleep)
    pyautogui.hotkey('ctrl', 'q')

# Quit
pyautogui.hotkey('ctrl', 'q')

#exit()
