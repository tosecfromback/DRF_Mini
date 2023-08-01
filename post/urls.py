from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Post Index
    path('',views.PostIndex.as_view(),name='index'),
    # Post List
    path('',views.PostList.as_view(), name='list'),
    # Post Search
    # path('',views.PostSearch.as_view(), name=search),
]