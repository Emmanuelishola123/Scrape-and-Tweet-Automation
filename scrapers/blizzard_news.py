# IMPORT NECCESSARY LIB
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tweeter.tweet import tweet



# PATH TO CHROMEDRIVER
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)



def blizzard_news_scrapper():
    driver.implicitly_wait(10)
    driver.get('https://playhearthstone.com/en-gb/news')

    a = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.Article-Link"))).click()
   
    # element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
    # driver.execute_script("arguments[0].click();", element)

    # element = driver.find_element_by_css('div[class*="loadingWhiteBox"]')
    # webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()

    title = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='heading--small heading--article']/span"))).text
    description = driver.find_element(By.XPATH, "//div[@class='detail blog-detail']/p").text

    intro = '📢---Forum news spotted---📢'
    desc = description
    url = driver.current_url

    print(intro)
    print(title)
    print(desc)
    print(url)

    # UPLOAD TO TWITTER
    tweet(intro, title, desc, url)
    
    time.sleep(5)
    driver.quit()

