from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /cats/ 경로에 대한 기본 뷰
    path('<str:name>/create/', views.cat_create, name='cat-create'),  # /cats/<name>/create/ 경로
]