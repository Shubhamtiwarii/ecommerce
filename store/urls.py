from django.urls import path 
from . import views

urlpatterns = [
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('store/',views.store,name='store'),
   # path('checkout/',views.checkout,name='checkout'),
    path('updatecart/',views.updateCart,name='updatecart'),
    path('updatequantity/',views.updateQuantity,name='updatequantity'),
    path("deleteProduct/",views.deleteProduct,name="deleteproduct"),
    path("address_and_payment/",views.address_and_payment,name="address_and_payment"),
    path('order/',views.order,name="order"),
    path('sign_up/',views.signup,name="signup"),
    path('login/', views.login, name='login'),
    path('logout/',views.logout_view,name="logout"),
]
