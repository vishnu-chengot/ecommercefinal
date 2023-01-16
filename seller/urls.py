from django.urls import path
from.import views 
app_name='seller'

urlpatterns=[
  path('home',views.home,name='home'),
  path('addproduct',views.add_product),
  path('changepassword',views.change_password),
  path('productcatalog',views.product_catalog),
  path('profile',views.profile),
  path('updatestock',views.update_stock,name='updatestock'),
  path('stock_number',views.stock_number,name='stock_number'),
  path('profile_ajax',views.profile_ajax,name='profile_ajax'),
]