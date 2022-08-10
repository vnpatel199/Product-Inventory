from django.shortcuts import render, redirect
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import Http404


# Create your views here.
def index(request):
    return render(request, "index.html")

@csrf_exempt
def search(request):
    if 'term' in request.GET:
        res = None
        qs = Product.objects.filter(product_name__icontains=request.GET.get('term'))
        titles = []
        for i in qs:
            item = {
                'name':i.product_name,
                'price': i.price,
                'image':i.photo.url
            }
            titles.append(item)
        res = titles
        return JsonResponse({'data':res})

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            raise Http404("Bad Credentials")
            
    return render(request, "login.html")