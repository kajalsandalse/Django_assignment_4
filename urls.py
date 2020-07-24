from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('AddRecordpage',views.AddRecordpage,name="AddRecordpage"),
    path('Recordpage',views.Recordpage,name="Recordpage"),
    path('check',views.getdata,name="getdata"),
]