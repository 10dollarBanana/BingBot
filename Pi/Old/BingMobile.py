import pandas
import pyautogui
import time
import webbrowser
import random
import requests


# Get trending values
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
trendsUS = pytrends.trending_searches(pn='united_states')
trendsUK = pytrends.trending_searches(pn='united_kingdom')
trendsAUS = pytrends.trending_searches(pn='australia')

# Convert to list
trendsUS = pandas.DataFrame(trendsUS)
trendsUK = pandas.DataFrame(trendsUK)
listUS = trendsUS.values.tolist()
listUK = trendsUK.values.tolist()
listAUS = trendsAUS.values.tolist()


# Merge two lists
list = (listUS + listUK + listAUS)

# Get unique values
output = []
for x in list:
    if x not in output:
        output.append(x)

url = 'https://www.bing.com/'


for i in range(25):
    count = i + 1
    pos = len(output) - 1
    time.sleep(10)
    search = output[pos - i]
    search = str(search)
    search = search.replace("['", "")
    search = search.replace("']", "")

    b = webbrowser.get('chromium-browser')
    b.open_new(url)
    time.sleep(2)
    pyautogui.hotkey('esc')
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(10)
    pyautogui.hotkey('tab')
    sleep = random.randint(5,30)
    time.sleep(sleep)
    pyautogui.typewrite(search, interval=0.01)
    pyautogui.typewrite('\n', interval=5)
    time.sleep(30)
    pyautogui.hotkey('alt', 'F4')
    print(f"The count is {count} with a pause of {sleep} seconds between searches. We searched for {search}")
