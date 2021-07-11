from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
  path('login/',login_view, name="login"),
  path('logout/',logout_view, name="logout"),
  path('register/',register_view,name="signup"),
  path('mypage/',mypage_view,name="mypage"),

  
]