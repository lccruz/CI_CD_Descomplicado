from django.urls import path

from product import views


urlpatterns = [
    path('', views.product_list, name='product-list'),
]
