
from django.urls import path, include
from . import views

urlpatterns = [
	path('',views.home , name ='home'),
    path('about/',views.about , name ='about'),
    path('add_stock.html/',views.add_stock_page, name ='add_stock'),
    path('delete/<stock_id>',views.delete, name ='delete'),

]