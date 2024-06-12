from django.urls import path,include
from . import views
urlpatterns = [
    path('/slot_book/<centerid>/<slot>/<vaccine>/<date>', views.slot_book,name='slot_book'),
    path('/slot_status', views.slot_status,name='slot_status'),
    path('/certificate', views.certificate,name='certificate'),
    path('/home', views.home,name='b_home'),
    
]