from django.shortcuts import render
from coinmarketcap import Market
from twitter import Twitter
#import twitter
import oauth2
#from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#import coinmarketcap
#from requests_oauthlib import OAuth1Session
#import json
#import settings

# Create your views here.
def home(request):
    coinmarketcap = Market()
    json_result = coinmarketcap.ticker(start=0, limit=10, convert='USD')

    result = []
    for j in json_result:
#        result_line = []
        result_line = {
            "id": j['id'],
            "name": j['name'],
            "symbol": j['symbol'].lower(),
            "rank": j['rank'],
            "price_usd": j['price_usd'],
            "market_cap_usd": j['market_cap_usd'],
            "percent_change_24h": j['percent_change_24h'],
            "percent_change_7d": j['percent_change_7d'],
        }
        result.append(result_line)
    return render(request, 'home.html',{'result':result})

def detail(request, id):
    #coinmarketcap
    coinmarketcap = Market()
    json_result = coinmarketcap.ticker(id, limit=10, convert='USD')

    """
    # ...
    twitter = Twitter(
      auth=OAuth(token, token_key, con_secret, con_secret_key))

    api = twitter.Api(consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET)
    home_timeline = api.VerifyCredentials()


    def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers=None):
        consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
        token = oauth2.Token(key=key, secret=secret)
        client = oauth2.Client(consumer, token)
        resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
        return content

    home_timeline = oauth_req('https://api.twitter.com/1.1/statuses/home_timeline.json', ACCESS_TOKEN, ACCESS_SECRET, "GET", "A" )

    twitter = OAuth1Session(settings.CONSUMER_KEY, settings.CONSUMER_SECRET, settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

    params = {}
    req = twitter.get("https://api.twitter.com/1.1/statuses/home_timeline.json", params = params)

    home_timeline = json.loads(req.text)
    return render(request, 'detail.html', {'json_result':json_result[0], 'home_timeline':home_timeline})
    """
    return render(request, 'detail.html', {'json_result':json_result[0]})

"""
def twitter_stream(request):
    # Initiate the connection to Twitter Streaming API
    twitter_stream = TwitterStream(auth=oauth)

    # Get a sample of the public data following through Twitter
    iterator = twitter_stream.statuses.sample()

    # Print each tweet in the stream to the screen
    # Here we set it to stop after getting 1000 tweets.
    # You don't have to set it to stop, but can continue running
    # the Twitter API to collect data for days or even longer.
    tweet_count = 1000
    for tweet in iterator:
        tweet_count -= 1
        # Twitter Python Tool wraps the data returned by Twitter
        # as a TwitterDictResponse object.
        # We convert it back to the JSON format to print/score
        print json.dumps(tweet)

        # The command below will do pretty printing for JSON data, try it out
        # print json.dumps(tweet, indent=4)

        if tweet_count <= 0:
            break
    return render(request, {})
"""

#print(result)
