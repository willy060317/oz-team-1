from django.urls import path
from .views import index, cat_create, health_record_create  # CatHealthRecordView 대신 health_record_create 사용

urlpatterns = [
    path('', index, name='cat-index'),  # GET 모든 Cat 목록
    path('cats/<str:name>/', cat_create, name='cat-create'),  # POST로 Cat 생성
    path('cats/<int:cat_id>/health-record/', health_record_create, name='cat-health-record'),  # POST로 건강 기록 추가
]