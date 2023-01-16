from django.shortcuts import render
from .models import Product
from common.models import seller
from django.http import JsonResponse

# Create your views here.
def home(request):
    seller_details = seller.objects.get(id=request.session['seller'])
    product = Product.objects.filter(seller_id =request.session['seller'])
    sname = seller_details.first_name+' '+seller_details.second_name
    context ={
       'name':sname,
       'products':product,
    }
    return render(request,'seller/home.html',context)
      

def add_product(request):
    if request.method == 'POST':
      p_name =request.POST['product_name']
      p_category = request.POST['product_category']
      p_number =request.POST['product_number']
      p_disc =request.POST['product_dis']
      p_quantity =request.POST['product_quantity']
      
      p_price =request.POST['product_price']
    
      p_img = request.FILES['product_img'] 
      seller = request.session['seller']
      new_product = Product(product_name =p_name,category_name =p_category,product_number =p_number,
      product_discription=p_disc,price =p_price,stock=p_quantity,image =p_img,seller_id = seller)
    
      
      new_product.save()

    return render(request,'seller/add product.html')

def change_password(request):
    error_msg = ''
    success_msg = ''
    if request.method == 'POST':
      old_password = request.POST['old_password']
      new_password = request.POST['new_password']
      conform_password = request.POST['conform_password']
      if new_password == conform_password:
        if len(new_password) > 8:
            Seller = seller.objects.get(id =request.session['seller'])
            if old_password == Seller.password:
                Seller.password = new_password
                Seller.save()
                success_msg = 'successfully created new password'
            else:
                error_msg ='invalid password'
        else:
            error_msg = 'password should be minimum 8 characters'
      else:
        error_msg ='password does\'t match'
    return render(request,'seller/change password.html',{'error':error_msg,'success':success_msg})
  
def product_catalog(request):
    return render(request,'seller/product catalog.html')

def profile(request):
    seller_details = seller.objects.get(id=request.session['seller'])
    return render(request,'seller/profile.html',{'profile':seller_details})

def update_stock(request):
    product = Product.objects.filter(seller_id =request.session['seller'])
    if request.method == 'POST':
        
        prodid =request.POST['pid']
        print(prodid)
        
        new_stock =request.POST['new_stock']
        product1 =Product.objects.get(id=prodid)
        product1.stock += int(new_stock)
        
        product1.save()
    return render(request,'seller/update stock.html',{'products':product})

def stock_number(request):
    qty = request.POST['qty']
    product = Product.objects.filter(id=qty).values('product_name','stock')
    p_name = product[0]['product_name']
    p_stock = product[0]['stock']
    return JsonResponse({'pname':p_name,'pstock': p_stock})

def profile_ajax(request):
    proid =request.POST['proid']
    profile = seller.objects.filter(id=proid).values('first_name','second_name','address')
    f_name =profile[0]['first_name'] 
    l_name =profile[0]['second_name']
    s_address =profile[0]['address']
    
    return JsonResponse({'fname':f_name,'l_name':l_name,'s_address':s_address})


    