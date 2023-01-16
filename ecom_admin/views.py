from django.shortcuts import render
from common.models import seller
from seller.models import Product

# Create your views here.

def home(request):
    return render(request,'ecom_admin/home.html')

def approveseller(request):
    return render(request,'ecom_admin/approve seller.html')
   
def viewcustomer(request):
    return render(request,'ecom_admin/view customer.html')  

def viewseller(request):
    return render(request,'ecom_admin/view seller.html')  

def view_product(request):
    all_product =Product.objects.all()

    return render(request,'ecom_admin/view_product.html',{'all_product':all_product})   