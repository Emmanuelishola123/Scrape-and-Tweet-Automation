# IMPORT NECCESSARY LIB
import os
import time
from scrapers.setup import format_description_text
from tweeter.tweet import tweet



trigger_Words = ['Trailer', 'Chat', 'Reveal', 'Announcement', 'Overview', 'Teaser', 'Adventure', 'Year', 'Update', 'Hearthstone']
c_path = os.getcwd()

def scrape_youtube(driver, WebDriverWait, By, EC):
    latest_video = None
    tweeted = False
    driver.implicitly_wait(10)
    driver.get('https://www.youtube.com/c/Hearthstone/videos')

    videos = WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a#video-title.yt-simple-endpoint.style-scope.ytd-grid-video-renderer")))
    time.sleep(0.5)

    for video in videos:
        if latest_video != None:
            break
        with open(c_path +"/data/data.txt") as f:
            for line in f:
                if line.strip() == video.get_attribute('href'):
                    tweeted = True
                    
        if tweeted:
            break
        title = video.get_attribute('title')
        print(title)
        for word in trigger_Words:
            if word.lower() in title.lower():
                with open(c_path +"/data/data.txt", "a") as file:
                    file.write(video.get_attribute('href') + '\n')
                latest_video = video
                print(word)
                break

    if latest_video == None:
        return print('No Latest video......')
    else:
        latest_video.click()
        
        time.sleep(5)

        intro = '📢--- New video spotted ---📢'
        description = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.style-scope.yt-formatted-string"))).text
        url = driver.current_url
        desc = format_description_text(description)

        text = f"{intro}\n\n📺 {title}\n\n\"{desc}\"\n\nSource: {url}"

        print('Youtube age...........................#####################################################')
        print(text)

        # UPLOAD TO TWITTER
        tweet(text)
        
        time.sleep(5)
        driver.quit()

