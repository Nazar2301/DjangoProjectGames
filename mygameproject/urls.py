from django.contrib import admin
from django.urls import path
from task1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('registration/', views.sign_up_by_django, name='registration'),
    path('platform/news/', views.news, name='news'),
]
