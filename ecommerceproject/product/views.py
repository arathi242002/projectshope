from django.shortcuts import render
from product.models import Products
from django.core.paginator import Paginator
# Create your views here.


def index(request):
    return render(request,'index.html')


def product_list(request):

    page=1
    if request.GET:
        page=request.GET.get('page',1)

    product_obj=Products.objects.order_by('priority')
    product_paginator=Paginator(product_obj,4)
    product_obj=product_paginator.get_page(page)
    context={'products':product_obj}
    return render(request,'product_list.html',context)


def product_details(request,pk):
    Product=Products.objects.get(pk=pk)
    context={'Product':Product}

    return render(request,'product_details.html',context)