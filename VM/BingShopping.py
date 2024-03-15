#!/usr/bin/python3

# Import
import time
import random
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Vars
url = 'https://www.msn.com/en-us/shopping'
type_int=0.2

EDGE_USER_AGENT = ('Mozilla/5.0'
                 'AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/114.0.0.0 Safari/537.36 Edge/114.0.1823.58')

# From: https://www.reddit.com/r/MicrosoftRewards/comments/10dpg01/msn_shopping_game_script/
js = "javascript:(async function(){var e=document.querySelector(\"shopping-page-base\")?.shadowRoot.querySelector(\"shopping-homepage\")?.shadowRoot.querySelector(\"msft-feed-layout\")?.shadowRoot.querySelector(\"msn-shopping-game-pane\");if(null!=e){e.style.gridArea=\"slot2\",window.scrollTo(0,0);var t=[];t=t.concat(await e.fetchGameDataFunc(),await e.fetchGameDataFunc(),await e.fetchGameDataFunc()),e.fetchGameDataFunc=async function(e){return[t[Math.floor(Math.random()*t.length)]]},window.startCountdownOG||(window.startCountdownOG=e.startCountdown,e.startCountdown=function(){window.startCountdownOG.call(e),setTimeout((()=>{if(!window.gameCounterElem){window.gameCounter=-1;var t=document.createElement(\"div\");t.className=\"view-leaderboard stats-game-counter\",t.style=\"right: unset; left: 25px; font-size: 13px;\",e.gameContainerRef.getElementsByClassName(\"game-panel-container\")[0].appendChild(t),window.gameCounterElem=t}window.gameCounter++,window.gameCounterElem.textContent=`Game: ${window.gameCounter}`}),1e3*e.gameSettings.newGameCountdown+1e3)}),e.getGameResult=function(t){if(t===e.selectedCardIndex)return localStorage.removeItem(\"gamesPerDay\"),e.dailyLimitReached=!1,e.leaderboardRecord&&(e.leaderboardRecord.dailyGuessingGamesPlayed=0),\"win\"===e.gameState?\"win\":\"lose\"},e.gameSettings.newGameCountdown=0,e.getGameResult(-1),e.gameState=\"win\",e.startCountdown(),e.startCountdown(),setTimeout((()=>{for(var t=0;t<=1e4;t++)clearInterval(t);e.gameSettings.newGameCountdown=6}),2200)}else alert(\"Unable to locate the shopping game!\\nRefresh the page and try again.\");})();"


def scroll_shim(passed_in_driver, object):
    x = object.location['x']
    y = object.location['y']
    scroll_by_coord = 'window.scrollTo(%s,%s);' % (
        x,
        y
    )
    scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
    passed_in_driver.execute_script(scroll_by_coord)
    passed_in_driver.execute_script(scroll_nav_out_of_way)
        
        
# Load Firefox
profile_path = '/home/jason/snap/firefox/common/.mozilla/firefox/mzuy6y63.default'
# profile_path = '/Users/jason/Library/Application Support/Firefox/Profiles/outve2dq.default'
ffOptions = Options()
ffOptions.add_argument("-profile")
# ffOptions.add_argument(r'/Users/jason/Library/Application Support/Firefox/Profiles/outve2dq.default')
ffOptions.add_argument(profile_path)
# driver = webdriver.Firefox(options=ffOptions)

# Set user agent
ffOptions.set_preference("general.useragent.override", EDGE_USER_AGENT)

# Load firefox
driver = webdriver.Firefox(options=ffOptions)

# Loop
for i in range(10):
    time.sleep(10)
    driver.get(url)
    sleep = random.randint(30,60)
    time.sleep(sleep)
    driver.execute_script(js)
    time.sleep(3)
    # Step 1 activate overlap
    # Find element using Java Script
    element = driver.execute_script('''return document.querySelector("shopping-page-base").shadowRoot.querySelector("shopping-homepage").shadowRoot.querySelector("msft-feed-layout").shadowRoot.querySelector("msn-shopping-game-pane").shadowRoot.querySelector("msft-stripe")''')
    element = element.find_element(By.XPATH, '//*[@class="shopping-overlay-container"]')
    scroll_shim(driver, element)
    time.sleep(3)
    # Hover
    action = ActionChains(driver)
    action.move_to_element(element).perform()
    time.sleep(3)
    # Step 2: Click select
    element = element.find_element(By.XPATH, '//*[@class="shopping-select-overlay-button"]')
    action.move_to_element(element).click().perform()
    time.sleep(3)

# Quit
driver.close()

open('shopping.complete', 'a').close()


