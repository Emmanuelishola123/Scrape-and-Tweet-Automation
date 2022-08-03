import time
from scrapers.shop_battle import battle_shop_scrapper
from scrapers.youtube import scrape_youtube


while True:
    # print('Scraping Youtube...........................')
    # scrape_youtube()

    # # Sleep for 5mins then continue
    # time.sleep(60 * 5)

    print('Scraping shop.battle.net...........................')
    battle_shop_scrapper()

    # Sleep for 5mins then continue
    time.sleep(60 * 5)

