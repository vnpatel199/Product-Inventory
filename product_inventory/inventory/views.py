import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.http import Http404
from django.contrib.auth.decorators import login_required


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
            return redirect('home')
        else:
            raise Http404("Bad Credentials")
            
    return render(request, "login.html")

def Logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/login/')
def home(request):
    product = Product.objects.all()
    print(product)
    return render(request, "home.html",{
        "product": product
    })

@login_required(login_url='/login/')
def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "detail.html", {'product':product})

@login_required(login_url='/login/')
def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product_name = request.POST['product_name']
        quantity = request.POST['quantity']
        price = request.POST['price']
        update = Product.objects.filter(pk=pk).update(product_name=product_name,quantity=quantity ,price=price)
        return redirect('home')

    return render(request, "update.html", {'product':product})


