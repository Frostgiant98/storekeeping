
from django.urls import path, include

from core import views

urlpatterns = [
    path('', views.homepage),
    path('items/', views.itemList),
    path('stores/', views.storeList),

    path('store-detail/<int:pk>/', views.storeDetail),
    path('item-detail/<int:pk>/', views.itemDetail),

    path('item/', views.itemCreate),
    path('store/', views.storeCreate),


    path('store-items/<int:pk>/', views.storeItems),



    # path('book/<str:pk>/', views.book_Detail_Update), # PUT update details and GET detail view
    # path('author/<str:pk>/', views.author_Detail_Update), # PUT update details and GET detail view


]
