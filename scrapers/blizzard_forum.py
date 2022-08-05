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




def blizzard_forum_scrapper(driver, WebDriverWait, By, EC):
    driver.implicitly_wait(10)
    driver.get('https://us.forums.blizzard.com/en/hearthstone/g/blizzard-tracker/activity/topics')

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='title raw-link raw-topic-link']"))).click()
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[@class='widget-link now-date']"))).click()

    latest = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='cooked']")))[-1]
    issue = latest.find_element(By.TAG_NAME, "p").text

    intro = '📢---Forum known issues update spotted---📢'
    url = driver.current_url
    p_text = format_description_text(issue)

    text = f"{intro}\n\n📺{p_text}\n\nSource: {url}"

    print('Blizzard Forum...........................#####################################################')
    print(text)

    # UPLOAD TO TWITTER
    tweet(text)
    
    time.sleep(5)
    driver.quit()
    
    
