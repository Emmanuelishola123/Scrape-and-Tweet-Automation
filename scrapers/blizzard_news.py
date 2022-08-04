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



def blizzard_news_scrapper():
    driver.implicitly_wait(10)
    driver.get('https://playhearthstone.com/en-gb/news')

    a = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='NewsListItem__ArticleListItem-sc-11gqdi2-0 bcLzKr ArticleListItem  NewsHomeApp__HomeNewsListItem-sc-173hfhu-2 jVJUNv']")))
   
    time.sleep(5)
    print(a.get_attribute('href'))
   



blizzard_news_scrapper()
