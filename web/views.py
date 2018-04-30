from django.shortcuts import render
from coinmarketcap import Market
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

#print(result)
