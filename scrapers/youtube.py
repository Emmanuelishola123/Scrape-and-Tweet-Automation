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
trigger_Words = ['Trailer', 'Chat', 'Reveal', 'Announcement', 'Overview', 'Teaser', 'Adventure', 'Year', 'Update', 'Hearthside']


def scrape_youtube():
    latest_video = None
    # title = ''
    # desc = ''
    # url = ''
    driver.implicitly_wait(10)
    driver.get('https://www.youtube.com/c/Hearthstone/videos')

    time.sleep(4)
    videos = driver.find_elements(By.XPATH, "//a[@id='video-title' and @class='yt-simple-endpoint style-scope ytd-grid-video-renderer']")
    time.sleep(0.5)

    for i in videos:
        if latest_video != None:
            break
        title = i.get_attribute('title')
        print(title)
        for word in trigger_Words:
            if word in title:
                latest_video = i
                print(word)
                break

    latest_video.click()
    
    time.sleep(5)

    desc = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[@class='style-scope yt-formatted-string']"))).text
    url = driver.current_url

    # print(title)
    # print(desc)
    # print(len(desc))
    # print(url)

    # UPLOAD TO TWITTER
    tweet(title, desc, url)
    
    time.sleep(5)
    driver.quit()