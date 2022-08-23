# IMPORT NECCESSARY LIB
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# CONFIG FOR DEVELOPMENT ENV
PATH = "C:\Program Files (x86)\chromedriver.exe"    # Replace with your chromedriver path 
driver = webdriver.Chrome(PATH)

# # CONFIG FOR PRODUCTION ENV
# op = webdriver.ChromeOptions()
# op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
# op.add_argument("--headless")
# op.add_argument("--no-sandbox")
# op.add_argument("--disable-dev-sh-usage")
# driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)


from scrapers.blizzard_forum import blizzard_forum_scrapper
from scrapers.blizzard_news import blizzard_news_scrapper
from scrapers.shop_battle import battle_shop_scrapper
from scrapers.youtube import scrape_youtube


while True:
    print('Scraping Youtube...........................')
    scrape_youtube(driver, WebDriverWait, By, EC)

    # Sleep for 5mins then continue
    # time.sleep( 10)


    # print('Scraping blizzard forum site...........................')
    # blizzard_forum_scrapper(driver, WebDriverWait, By, EC)

    # Sleep for 5mins then continue
    # time.sleep(10)


    # print('Scraping blizzard news site...........................')
    # blizzard_news_scrapper(driver, WebDriverWait, By, EC)

    # Sleep for 5mins then continue
    # time.sleep(10)

    # print('Scraping shop.battle.net...........................')
    # battle_shop_scrapper(driver, WebDriverWait, By, EC)

    # Sleep for 1 hour then continue
    time.sleep(60 * 60)

