from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('service/<pk>', ProductDetail.as_view(), name='details'),
    path('service', AllProduct.as_view(), name='service'),
    path('firma', AllFirma.as_view(), name='firma'),
    path('register', Registration.as_view(), name='register'),
    path('login', LoginViewMy.as_view(), name='login'),
    path('profile/<pk>', ProfileView.as_view(), name='profile'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('search_result', SearchResult.as_view(), name='result')
]