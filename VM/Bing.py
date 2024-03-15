#!/usr/bin/python3

import pyautogui
import time
import webbrowser
import random
from pytrends.request import TrendReq
import json

config="about:config"
url = 'https://www.bing.com/'
type_int=0.2

EDGE_USER_AGENT = ('Mozilla/5.0'
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134')

MOBILE_USER_AGENT = ('Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; WebView/3.0) '
                     'AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/64.118.222 '
                     'Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.15063')

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


def get_trending():
    # Get trending values
    pytrends = TrendReq(hl='en-US', tz=360)
    trendsUS = pytrends.trending_searches(pn='united_states')
    trendsUK = pytrends.trending_searches(pn='united_kingdom')
    trendsAUS = pytrends.trending_searches(pn='australia')
    trendsSA = pytrends.trending_searches(pn='south_africa')
    # Convert to list
    listUS = trendsUS.values.tolist()
    listUK = trendsUK.values.tolist()
    listAUS = trendsAUS.values.tolist()
    listSA = trendsSA.values.tolist()
    # Merge lists
    list = (listUS + listUK + listAUS + listSA)
    # Get unique values
    output = []
    for x in list:
        if x not in output:
            output.append(x)

    return output


output = get_trending()

time.sleep(3)
user_agent_switcher(EDGE_USER_AGENT)
time.sleep(3)

sleep = random.randint(0,300)
time.sleep(sleep)


# Loop
# Edge
for i in range(35):
    count = i + 1

    search = output[i]
    search = str(search)
    search = search.replace("['", "")
    search = search.replace("']", "")

    b = webbrowser.get('firefox')
    b.open_new_tab(url)
    sleep = random.randint(10,15)
    time.sleep(sleep)
    pyautogui.typewrite(search, interval=type_int)
    pyautogui.typewrite('\n', interval=5)
    pyautogui.hotkey('ctrl', 'q')

##################################################################
sleep = random.randint(30,120)
time.sleep(sleep)
user_agent_switcher(MOBILE_USER_AGENT)
##################################################################

# Mobile
for i in range(25):
    count = i + 1
    pos = len(output) - 1
    time.sleep(10)
    search = output[pos - i]
    search = str(search)
    search = search.replace("['", "")
    search = search.replace("']", "")

    b = webbrowser.get('firefox')
    b.open_new(url)
    time.sleep(2)
    pyautogui.hotkey('esc')
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(5)
    # pyautogui.hotkey('tab')
    sleep = random.randint(5,10)
    time.sleep(sleep)
    pyautogui.typewrite(search, interval=type_int)
    pyautogui.typewrite('\n', interval=5)
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'q')

time.sleep(2)
user_agent_switcher(EDGE_USER_AGENT)

# Quit
pyautogui.hotkey('ctrl', 'q')
time.sleep(30)

open('search.complete', 'a').close()

