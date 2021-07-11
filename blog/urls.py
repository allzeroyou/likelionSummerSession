from django.urls import path
from .views import *

urlpatterns = [

    path('<str:id>',detail,name="detail"),#str=자료형, id=매개변수의 이름
    path('new/', new, name="new"),
    path('create/',create,name="create"),
    path('edit/<str:id>',edit,name="edit"),
    path('update/<str:id>',update,name="update"),
    path('delete/<str:id>',delete,name="delete"),
]