from . import views
from django.urls import path

app_name = 'shop'

urlpatterns = [
    path('', views.allproduct, name='allproduct'),
    path('<slug:c_slug>/', views.allproduct, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProDetail, name='proCatdetail'),
]
