import tweepy

from scrapers.setup import format_description_text


# Store Credentials
consumer_key = 'peerwaI29wPMr8ahRh7kANhgK'
consumer_secret = 'q95DpQNXsj2gsa6t2a6FaJMUtJ9X6DzOBWpkbBBngdr5X1qlq7'

access_token = '1549187609523519489-6Mdu9bZeYE61MJsOEryBy5HVY6HtPU'
access_token_secret = '0XJg483kFOhWpxDbJBWcAjI504EJP30SfBBSWQQE0sXva'


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)



# The app and the corresponding credentials must have the Write permission
def tweet(intro, title, description, url):
  
    desc = format_description_text(description)

    text = f"{intro}\n\n📺{title}\n\n\"{desc}\"\n\nSource:\n{url}"
    print(text)
    print(len(text))
    response = client.create_tweet(
        text = f"{intro}\n\n📺{title}\n\n\"{desc}\"\n\nSource:\n{url}"
    )
    print(f"https://twitter.com/user/status/{response.data['id']}")



