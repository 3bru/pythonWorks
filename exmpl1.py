""""from math import *
x = 89*9144
print(x)"""

from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time


def gogol(keyword):
    profile = webdriver.FirefoxProfile()
    profile.native_events_enable = True

    driver = webdriver.FirefoxProfile(profile)
    searchEngineUrl = "http://www.google.com"

    driver.get(searchEngineUrl)
