from django.urls import path
from . import views
from stores.models import Product

urlpatterns = [
    path("hello/", views.say_hello),
    path('greet/',views.say_goodmorning),
    path('prods/', views.get_prods),
    path('delete/', views.delete_all)
    # path("", views.welcome_msg),
]
