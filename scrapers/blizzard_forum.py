# IMPORT NECCESSARY LIB
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from tweeter.tweet import tweet


# PATH TO CHROMEDRIVER
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)




def blizzard_forum_scrapper():
    driver.implicitly_wait(10)
    driver.get('https://us.forums.blizzard.com/en/hearthstone/g/blizzard-tracker/activity/topics')


    a = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='title raw-link raw-topic-link']"))).click() 
    

blizzard_forum_scrapper()