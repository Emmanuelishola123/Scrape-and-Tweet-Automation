# IMPORT NECCESSARY LIB
import os
import time
from scrapers.setup import format_description_text
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from tweeter.tweet import tweet

path = os.getcwd()
default_media = 'https://pbs.twimg.com/media/Fab5GYZXoAYIuYn?format=png&name=small'

# PATH TO CHROMEDRIVER
# PATH = "C:\Program Files (x86)\chromedriver.exe"
# driver = webdriver.Chrome(PATH)




def blizzard_forum_scrapper(driver, WebDriverWait, By, EC):
    driver.implicitly_wait(10)
    driver.get('https://us.forums.blizzard.com/en/hearthstone/g/blizzard-tracker/activity/topics')

    url = None 

    all_bliss_articles = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.tracked-post.group-community-manager")))
    top_ten_articles = all_bliss_articles[:10] 

    for new_url in top_ten_articles:
        tweeted = False
        with open(path +"/data/tweeted_articles.txt") as f:
            for line in f:
                if line.strip() == new_url.get_attribute('href'):
                    tweeted = True
                    break
        if tweeted:
            continue  
        else: 
            with open(path +"/data/tweeted_articles.txt", 'a') as f:
                f.write(new_url.get_attribute('href') + '\n')
                url = new_url.get_attribute('href')
            break

    if url == None:
        print('No new articles available at the moment')        
    else:
        scrape_articles(driver, WebDriverWait, By, EC, url)
        driver.quit()
        print('done..............')    


def scrape_articles(driver, WebDriverWait, By, EC, url):
    driver.get(url)
    time.sleep(10)
    title = driver.find_element(By.CSS_SELECTOR, "a.fancy-title").text

    intro = '📢---Forum known issues update spotted---📢'
    url = driver.current_url
   
    text = f"{intro}\n\n📺 {title}\n\nSource: {url}"

   
    # UPLOAD TO TWITTER
    tweet(text, media = default_media)
    
    time.sleep(5)
    driver.quit()
    
    
