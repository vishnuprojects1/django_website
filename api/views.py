from rest_framework.response import Response
from rest_framework.decorators import api_view
from vishome.models import item
from vishome.models import contactdet
from .serializers import ItemSerializer
from .serializers import ContactdetSerializer
from rest_framework import status

@api_view(['GET'])
def getData(req,format=None):
    items=item.objects.all()
    serializer=ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(req,format=None):
    serializer=ItemSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def item_detail(req,id,format=None):
    try:
        items=item.objects.get(pk=id)
    except item.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method == 'GET':
        serializer=ItemSerializer(items)
        return Response(serializer.data)
    elif req.method == 'PUT':
        serializer=ItemSerializer(items,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif req.method == 'DELETE':
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET'])
def contactData(req,format=None):
    items=contactdet.objects.all()
    serializer=ContactdetSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addContact(req,format=None):
    serializer=ContactdetSerializer(data=req.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def contact_detail(req,id,format=None):
    try:
        items=contactdet.objects.get(pk=id)
    except contactdet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if req.method == 'GET':
        serializer=ContactdetSerializer(items)
        return Response(serializer.data)
    elif req.method == 'PUT':
        serializer=ContactdetSerializer(items,data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif req.method == 'DELETE':
        items.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

