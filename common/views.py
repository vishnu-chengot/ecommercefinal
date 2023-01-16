from django.shortcuts import render ,redirect
from .models import Customer
from .models import seller
from random import randint
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request,'common/master.html')

def customer_login(request):
    return render(request,'common/home.html')

def customer_signup(request):
    if request.method == 'POST':
        f_name =request.POST['customerfirstname']
        l_name = request.POST['customerlastname']
        c_address =request.POST['customeraddress']
        c_phone =request.POST['customerphone']
        c_email =request.POST['customeremail']
        c_password =request.POST['customerpassword']
        new_customer = Customer(first_name=f_name,second_name=l_name,email=c_email,password=c_password,phone=c_phone,address=c_address)
        new_customer.save()

    return render(request,'common/customer signup.html')

def project_home(request):
    return render(request,'common/project home.html')

def seller_login(request):
    
    msg = ''
    if request.method  == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try: 
            Seller = seller.objects.get(user_name = email, password = password)   #model_name= post_name
            request.session['seller'] = Seller.id
            return redirect('seller:home') #redirect(app_name:url_name)
        except Exception as e:
            print (e)   #to check error
            msg = 'Invalid credentials'

    


    return render(request,'common/seller login.html',{'message':msg})

def seller_signup(request):
    if request.method == 'POST':
      f_name =request.POST['sellerfirstname']
      l_name = request.POST['sellerlastname']
      s_address =request.POST['selleraddress']
      s_phone =request.POST['sellerphone']
      s_email =request.POST['selleremail']
      
      s_bankname =request.POST['sellerbankname']
      user_name1 = randint(1111,9999)
      s_password = 'sell-'+str(user_name1)+'-'+s_phone[6:10]
      s_accountnum =request.POST['selleraccountnumber']
      s_ifsc =request.POST['sellerifsc'] 
      s_img = request.FILES['sellerimg'] 
      new_seller = seller(first_name=f_name,second_name=l_name,email=s_email,password=s_password,phone=s_phone,address=s_address,
      bank_name =s_bankname,account_number=s_accountnum,ifsc=s_ifsc,seller_pic=s_img,user_name=user_name1)
      email_subject = 'Account username and password'
      email_content = 'hai your username will be:  '+ str(user_name1)+' and password will be: '+s_password
      send_mail(
        email_subject,
        email_content,
        settings.EMAIL_HOST_USER,
        [s_email,],
        fail_silently = False
      )
      new_seller.save()
      
 
    return render(request,'common/seller signup.html')

def customer_login(request):
    msg = ''
    if request.method  == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try: 
            customer = Customer.objects.get(email = email, password = password)   #model_name= post_name
            request.session['customer'] = customer.id
            return redirect('customer:home') #redirect(app_name:url_name)
        except Exception as e:
            print (e)   #to check error
            msg = 'Invalid credentials'

    return render(request,'common/customer_login.html',{'message':msg})
    # return render(request,'common/customer_login.html')