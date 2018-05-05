from django.shortcuts import render
from coinmarketcap import Market
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#import coinmarketcap

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
            "symbol": j['symbol'],
            "rank": j['rank'],
            "price_usd": j['price_usd'],
            "market_cap_usd": j['market_cap_usd'],
            "percent_change_24h": j['percent_change_24h'],
            "percent_change_7d": j['percent_change_7d'],
        }
        result.append(result_line)
    return render(request, 'home.html',{'result':result})

def detail(request, id):
    coinmarketcap = Market()
    json_result = coinmarketcap.ticker(id, limit=10, convert='USD')
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
