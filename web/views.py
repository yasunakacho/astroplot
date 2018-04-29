from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{})


def detail(request, id):
    return render(request, 'detail.html', {'json_result':json_result[0]})
