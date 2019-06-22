from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('input/', views.input), # 사용자 입력 페이지
    path('output/', views.output) # 데이터 저장 페이지
]