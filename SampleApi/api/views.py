from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item
from .serializers import ItemSerializer
# Create your views here.


@api_view(['GET'])
def getData(request):
    # person={'name':'Dennis', 'age':28}
    item=Item.objects.all()
    serializer=ItemSerializer(item, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer=ItemSerializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)