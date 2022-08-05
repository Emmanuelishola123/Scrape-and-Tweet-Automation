# IMPORT NECCESSARY LIB
import time
from scrapers.setup import format_description_text
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from tweeter.tweet import tweet







# PATH TO CHROMEDRIVER
# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)



def blizzard_news_scrapper(driver, WebDriverWait, By, EC):
    driver.implicitly_wait(10)
    driver.get('https://playhearthstone.com/en-gb/news')

    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a.Article-Link"))).click()
    title = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='heading--small heading--article']/span"))).text
    description = driver.find_element(By.XPATH, "//div[@class='detail blog-detail']/p").text
    intro = '📢---Forum news spotted---📢'
    url = driver.current_url
    desc = format_description_text(description)

    text = f"{intro}\n\n📜{title}\n\n\"{desc}\"\n\nSource: {url}"

    print('Blizzard News...........................#####################################################')
    print(text)

    # UPLOAD TO TWITTER
    tweet(text)
    
    time.sleep(5)
    driver.quit()

