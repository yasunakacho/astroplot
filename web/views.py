from django.shortcuts import render, redirect
from coinmarketcap import Market
from twitter import Twitter
from twython import Twython
from .models import Cryptocurrency, Price, Alert
from datetime import date, datetime, timedelta



from .forms import AlertForm

from django.contrib.auth.models import User

import oauth2
import secrets
import os
#import twitter
#from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream
#import coinmarketcap
#from requests_oauthlib import OAuth1Session
#import json
#import settings

from django.contrib import auth
import requests
from .symbols import CRYPTO_NAME_TO_SYMBOL



# Create your views here.
def home(request):
    coinmarketcap = Market()
    json_result = coinmarketcap.ticker(start=0, limit=10, convert='USD')

    result = []
    for j in json_result:
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

#def login(request):
#    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    #return render(request, 'home.html')
    return redirect('/')

#how did we define id as a coin name?
def detail(request, id):
#   print(id, 'this is id')
    #coinmarketcap
    coinmarketcap = Market()
    json_result = coinmarketcap.ticker(id, limit=10, convert='USD')
    t = Twython(secrets.TWITTER_APP_KEY,
            secrets.TWITTER_APP_KEY_SECRET,
            secrets.TWITTER_ACCESS_TOKEN,
            secrets.TWITTER_ACCESS_TOKEN_SECRET)
    search = t.search(q='#bitcoin',count=100)
    cryptocurrency = Cryptocurrency.objects.get(name=id)
    #cryptocurrency = Cryptocurrency.objects.get(name=json_result.name)
    #cryptocurrency = Cryptocurrency.objects.filter(name=name)
    #date = Price.date
    #price = Price.open
    #get,filter,all
    #the next challnge is coin_id=id
    #price1 = Price.objects.all()
    price = Price.objects.filter(coin_id=cryptocurrency.id).order_by('-date')
#    import pdb; pdb.set_trace()
    price_list = list(price)
#    result = []
#    for data in price_list:
#        result_line = {
#            "date": data['date'],
#            "open": data['open'],
#        }
#        result.append(result_line)

    price_open = [float(a_price.open) for a_price in price_list]
    price_date = ["{:'%Y-%m-%d'}".format(a_price.date) for a_price in price_list]

    # str to date
    #date_str = 'Jun 16, 2018'
    #dt = datetime.strptime(data_str, '%b %d, %Y')
    #dt_formatted = str(dt.year) + '-' + str(dt.month) + '-' + str(dt.day)
    #=> 2018-6-16
    #https://github.com/kaeken1jp/snippets/blob/master/python.md

    #this line is simply trying to update sqlite
    #price = Price.objects.get(coin_id=1)
    #print(list_price, 'this is prices')
    print(price_open[0:20], 'this is prices')
    print(price_date[0:20], 'this is dates')
    #print (result, 'this is dates')
    #print (result.open, 'this is open')

    tweets = search['statuses']
    create_form = AlertForm()
    create_form.fields['user'].initial = request.user.id
    create_form.fields['coin'].initial = cryptocurrency.id

    ########################################################
    # Sample code to render chart from the API reuslt
    # Comment out the block for normal functioning
    symbol = CRYPTO_NAME_TO_SYMBOL[cryptocurrency.name]
    coinmarketcap_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    params = {'symbol': symbol}
    headers = {'X-CMC_PRO_API_KEY': '93b1776a-1c2f-4795-a84f-3dc198c3a63e'}
    r = requests.get(coinmarketcap_url, params=params, headers=headers)
    result = r.json()
    usd_quote = result['data'][symbol]['quote']['USD']
    price = usd_quote['price']
    date = usd_quote['last_updated']

    price_open = [price]
    price_date = [date]


    ########################################################

    params = {'json_result':json_result[0],
              'cryptocurrency':cryptocurrency,
              'price_open':price_open[0:31],
              'price_date':price_date[0:31],
              'create_form':create_form,
             }
    return render(request, 'detail.html', params)


def alert(request, id):
    user_id = request.POST.get('user')
    coin_id = request.POST.get('coin')
    high_price = request.POST.get('high_price')
    low_price = request.POST.get('low_price')
    # TODO : debug
    alert_count = Alert.objects.filter(user=user_id) \
                      .filter(coin=coin_id).count()
    alert_count = str(alert_count)
    print(alert_count)
    #messages.sccuss(request, alert_count)
    cc = Cryptocurrency.objects.get(id=id)
    return redirect(to='/detail/'+cc.name)
