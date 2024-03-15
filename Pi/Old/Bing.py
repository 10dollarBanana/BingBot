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


for i in range(30):
    count = i + 1

    search = output[i]
    search = str(search)
    search = search.replace("['", "")
    search = search.replace("']", "")

    b = webbrowser.get('firefox')
    b.open_new_tab(url)
    sleep = random.randint(10,11)
    time.sleep(sleep)
    pyautogui.typewrite(search, interval=0.01)
    pyautogui.typewrite('\n', interval=5)
    pyautogui.hotkey('shift', 'ctrl', 'w')
    print(f"The count is {count} with a pause of {sleep} seconds between searches. We searched for {search}")
