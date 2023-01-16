from django.shortcuts import render,redirect
from common.models import Customer
from seller.models import Product
from customer.models import cart
from django.http import JsonResponse
from .decorator import auth_customer

# Create your views here.
def home(request):
    customer_details = Customer.objects.get(id=request.session['customer'])
    product = Product.objects.all()
    cname = customer_details.first_name+' '+customer_details.second_name
    context = {
        'name':cname,
        'products':product,
    }
    return render(request,'customer/home.html',context)

def change_password(request):
    error_msg =''
    success_msg =''
    if request.method == 'POST':
       old_password =request.POST['old_password'] 
       new_password =request.POST['new_password']
       conform_password =request.POST['conform_password']
       if new_password == conform_password:
        if len(new_password) > 8:
            customer = Customer.objects.get(id =request.session['customer'])
            if old_password == customer.password:
                Customer.objects.filter(id =request.session['customer']).update(password =new_password)
                success_msg = 'successfully created new password'
            else:
                error_msg ='invalid password'
        else:
            error_msg = 'password should be minimum 8 characters'
       else:
        error_msg ='password does\'t match'
    return render(request,'customer/change password.html',{'erorr':error_msg,'success':success_msg} )

def checkout(request):
    return render(request,'customer/checkout.html')


@auth_customer
def my_cart(request):
    
    Cart =cart.objects.filter(customer_id =request.session['customer'])
   
    return render(request,'customer/my cart.html',{'cart':Cart})

def my_order(request):
    return render(request,'customer/my order.html')

def product_details(request,pid):
    product_details = Product.objects.get(id=pid)
    msg =''
    if request.method == 'POST':
        item =cart.objects.filter(customer=request.session['customer'],Product=pid).exists()
        if not item:

            cart_item = cart(customer_id =request.session['customer'],Product_id =pid)
            cart_item.save()
            return redirect('customer:cart1')
        else:
            msg='items already in cart'    
    return render(request,'customer/product details.html',{'details':product_details,'message':msg})
    

def profile(request):
    msg =""
    if request.method == 'POST':
      if request.POST['First_name'] and request.POST['Last_name'] and request.POST['address']:
        fname = request.POST['First_name']
        sname = request.POST['Last_name']
        address = request.POST['address']
        Customer.objects.filter(id =request.session['customer']).update(first_name=fname,second_name=sname,address=address)
        msg='Profile updated successfully'
           
      else:
       msg = 'please fill all the field before submitting'
        # print('No name submitted')
        
    customer_details = Customer.objects.get(id=request.session['customer'])

    return render(request,'customer/profile.html',{'profile':customer_details,'message':msg})


def master(request):
    return render(request,'customer/master.html')

def get_total(request):
    pid = request.POST['pid'] #pid is the [key] passed from ajax request
    qty = request.POST['qty']
    product = Product.objects.filter(id=pid).values('price')
    total_amount = int(qty)*product[0]['price']
    print(total_amount)
    return JsonResponse({'amount': total_amount})

def remove_cart_item(request,cid):
    item = cart.objects.get(id=cid)
    item.delete()
    return redirect('customer:cart1')

def log_out(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common:cmaster')


def profile_ajax(request):
    proid = request.POST['proid']
    customer = Customer.objects.filter(id=proid).values('first_name','second_name','address')
    f_name =customer[0]['first_name']
    s_name =customer[0]['second_name']
    c_add =customer[0]['address']
    return JsonResponse({'f_name': f_name,'s_name': s_name,'c_add': c_add,})