# You have to pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



PIN_CODE = ""
i = 0

PIN_CODE = input("Enter Kahoot game PIN-Code: ")
BOT_AMOUNT = input("How many bots would you like to add: ")

while i < int(BOT_AMOUNT):
    BROWSER = webdriver.Edge(
        r'C:\\path\\to\\msedgedriver.exe') # Path to browser driver, I have used edge
    BROWSER.get('https://kahoot.it/')
    PIN_TYPING = BROWSER.find_element_by_id("game-input")
    PIN_TYPING.send_keys(PIN_CODE)
    PIN_TYPING.send_keys(Keys.RETURN)
    time.sleep(1)
    NICK_TYPING = BROWSER.find_element_by_id("nickname")
    NICK_TYPING.send_keys(i)
    NICK_TYPING.send_keys(Keys.RETURN)
    i = i + 1 
