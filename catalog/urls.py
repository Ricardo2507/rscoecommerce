from django.urls import path, include
from django.conf.urls import url
from . import views


app_name='catalog'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug>/', views.category, name='category'),
    #url(r'^(?P<slug>[\w_-]+)/$', views.category, name='category'),
    path('produtos/<slug>/', views.product, name='product'),
   
]