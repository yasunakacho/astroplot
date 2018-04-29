from django.shortcuts import render
import coinmarketcap

# Create your views here.
def home(request):
    market = coinmarketcap.Market()
    json_result = market.ticker('', limit=10, convert='USD')

    result = []
    for j in json_result:
        result_line = []
        result_line = {
            "id": j['id'],
            "name": j['name'],
            "price_usd": j['price_usd'],
            "percent_change_24h": j['percent_change_24h'],
            "percent_change_7d": j['percent_change_7d'],
        }
        result.append(result_line)
    return render(request, 'home.html',{'result':result})

def detail(request, id):
    market = coinmarketcap.Market()
    json_result = market.ticker(id, limit=10, convert='USD')
    return render(request, 'detail.html', {'json_result':json_result[0]})

#print(result)
