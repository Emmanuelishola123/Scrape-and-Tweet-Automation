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
    card_park_section = div.find_elements(By.CSS_SELECTOR, "section.ng-star-inserted")[2]
    ul = card_park_section.find_element(By.CSS_SELECTOR, "ul.browsing-card-group__layout")
    li = ul.find_element(By.CSS_SELECTOR, "li.browsing-card-group__layout--card")
    a = li.find_element(By.CSS_SELECTOR, "a.ng-star-inserted")

    print(a.get_attribute('href'))
    print(a.get_attribute('class'))
    time.sleep(2)   
    a.click()

    time.sleep(10)
    title = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='meka-font-display meka-font-display--header-4']/span"))).text
    price = driver.find_element(By.XPATH, "//div[@class='meka-price-label--details__price']/span").text
    availability = driver.find_element(By.XPATH, "//dd[@class='product-notification meka-font-body']").text
    desc = driver.find_element(By.XPATH, "//div[@class='product-heading']/p/p").text



    print(title)
    print(desc)
    print(availability)
    print(price)




    # a.click()
    # time.sleep(20)
    # print(driver.current_url)

    # time.sleep(5)
    # driver.close()


battle_shop_scrapper()
    





