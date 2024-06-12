from django.urls import path,include
from . import views
urlpatterns = [
     path('', views.home,name='home'),
     path('contactus', views.contact_us,name='contact_us'),
     path('login', views.login,name='login'),
     
     path('logout', views.logout,name='logout'),
     path('centres', views.centres,name='centres'),
     path('findslot', views.findslot,name='findslot'),
    
     
]