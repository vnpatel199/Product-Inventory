from django.shortcuts import render
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def index(request):
    return render(request, "index.html")

@csrf_exempt
def search(request):
    if 'term' in request.GET:
        qs = Product.objects.filter(product_name__icontains=request.GET.get('term'))
        titles = list()
        for i in qs:
            titles.append(i.product_name)
        return JsonResponse(titles, safe=False)