from django.contrib import admin
from django.urls import path
from . import views

app_name = 'gpt'

urlpatterns = [
    # GPT Index
    path('',views.GPTIndex.as_view(),name='index'),
    # Post List
    # path('',views.PostList.as_view(), name='list'),
    # Post Search
    # path('',views.PostSearch.as_view(), name=search),
]