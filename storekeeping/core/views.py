from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Item, Store
from .serializers import ItemSerializer, StoreSerializer

# from django.db.models import Count, Q
# from django.shortcuts import redirect, render, get_object_or_404
# from django.utils import timezone
# from django.urls.base import reverse
# from django.core.paginator import Paginator
# from django.contrib.admin.views.decorators import  staff_member_required
# from django.contrib.auth.decorators import user_passes_test

# Create your views here.


    # def homepage(request):


    #     return JsonResponse(request.__str__() , safe=False)

@api_view(["GET"])
def homepage(request):
    api_urls = {
        'Item List':'/items/',
		'Item Detail':'/item/<str:pk>/',
    } 
    return Response(api_urls)



@api_view(['GET'])
def itemList(request):
    tasks = Item.objects.select_related('store').order_by('item_id')
    # serializer = str(tasks.values())
    serializer = ItemSerializer(tasks, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def storeList(request):
    tasks = Store.objects.all().order_by('store_name')
    serial = StoreSerializer(tasks, many = True)
    return Response(serial.data)

@api_view(['GET'])
def storeItems(request, pk):
    tasks = Item.objects.select_related('store').filter(store_id = pk)
    serial = ItemSerializer(tasks, many = True)

    # return JsonResponse(str(tasks.values()), safe=False)
    return Response(serial.data)


@api_view(['GET'])
def itemDetail(request, pk):
	tasks = Item.objects.get(item_id=pk)
	serializer = ItemSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['GET'])
def storeDetail(request, pk):
	tasks = Store.objects.get(item_id=pk)
	serializer = StoreSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def itemUpdate(request, pk):
    task = Item.objects.get(item_id=pk)
    serializer = ItemSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        print(serializer)
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def storeUpdate(request, pk):
	task = Store.objects.get(store_id=pk)
	serializer = StoreSerializer(instance=task, data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def itemCreate(request):
	serializer = ItemSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def storeCreate(request):
	serializer = StoreSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['DELETE'])
def storeDelete(request):
	serializer = StoreSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)


@api_view(['DELETE'])
def itemDelete(request, pk):
	serializer = Store.objects.get(item_id=pk)
	serializer.delete()
	return Response(serializer.data)