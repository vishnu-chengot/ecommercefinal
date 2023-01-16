from django.urls import path
from.import views
app_name='common'

urlpatterns=[
  path('master',views.home,name='cmaster'),
  path('home',views.customer_login,name='chome'),
  path('customersignup',views.customer_signup,name='customer_signup'),
  path('projecthome',views.project_home,name='home'),
  path('sellerlogin',views.seller_login,name='seller_login'),
  path('sellersignup',views.seller_signup,name='seller_signup'),
  path('customer_login',views.customer_login,name='customer_login'),
]