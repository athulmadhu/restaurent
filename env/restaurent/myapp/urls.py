from . import views
from django.urls import path

urlpatterns = [
    path('',views.indexpage,name='index'),
    path('contact',views.contactpage,name='contact'),
    path('about',views.aboutpage,name='about'),
    path('booking',views.bookingpage,name='booking'),
    path('menu',views.menupage,name='menu'),
    path('addmenu',views.addmenu,name='addmenu'),
    path('customerreg',views.customerreg,name='customerreg'),
    
]
