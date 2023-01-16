from django.urls import path
from. import views 
app_name='customer'

urlpatterns=[
 path('home',views.home,name='home'),
 path('changepassword',views.change_password,name='changepassword'),
 path('checkout',views.checkout),
 path('mycart',views.my_cart,name='cart1'),
 path('myorder',views.my_order),
 path('productdetails/<int:pid>',views.product_details,name="productdetails1"),
 path('profile',views.profile,name='profile'),
 path('master',views.master),
 path('get_total',views.get_total,name='get_total'),
 path('remove_cart/<int:cid>',views.remove_cart_item,name='remove_cart_item'),
 path('logout',views.log_out,name='logout'),
 path('profile_ajax',views.profile_ajax,name='profile_ajax'),
]
