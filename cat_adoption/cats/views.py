from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cat
from .serializers import CatSerializer, HealthRecordSerializer

@api_view(['GET'])
def index(request):
    cats = Cat.objects.all()
    serializer = CatSerializer(cats, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def cat_create(request, name):
    if request.method == 'POST':
        data = request.data.copy()
        data['name'] = name
        serializer = CatSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def health_record_create(request, cat_id):
    if request.method == 'POST':
        data = request.data.copy()
        data['cat'] = cat_id
        serializer = HealthRecordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)