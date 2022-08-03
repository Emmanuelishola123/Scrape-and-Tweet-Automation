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



def battle_shop_scrapper():
    driver.implicitly_wait(10)
    driver.get('https://us.shop.battle.net/en-gb/family/hearthstone')

    # main = driver.find_element(By.XPATH, "//main[@id='main-content-skip-link-anchor']")
    
    main = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//main[@id='main-content-skip-link-anchor']")))
    div = main.find_element(By.XPATH, "//div[@id='start-of-content']")
    card_park_section = div.find_elements(By.XPATH, "//section[@class='ng-star-inserted']")[3]
    a = card_park_section.find_element(By.XPATH, "//a[@class='ng-star-inserted']")


    # ul = div.find_element(By.XPATH, "//ul[@class='browsing-card-group__layout']")
    # li = ul.find_element(By.XPATH, "//li[@class='browsing-card browsing-card-group__layout--card ng-star-inserted']")
    # a = li.find_element(By.XPATH, "//a[@class='ng-star-inserted']")


    print(a)


    # a.click()
    # time.sleep(20)
    # print(driver.current_url)

    # time.sleep(5)
    # driver.close()


battle_shop_scrapper()
    





