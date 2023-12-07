from django.urls import path
from myapp import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('addproduct/',views.addproduct_view,name='addproduct'),
    path('product/<str:product_id>/',views.product_view,name='productview'),
]
