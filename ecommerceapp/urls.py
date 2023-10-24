from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:id>/',views.detail_view,name='detail_view'),
    path('checkout/',views.checkout,name='checkout'),
]