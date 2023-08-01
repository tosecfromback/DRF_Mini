from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate
from gpt.models import QnA

# Create your views here.

### Post Index
class PostIndex(View):
    def get(self, request):
        context = {
            'title' : 'Post Index'
        }
        return render(request, 'post/post_index.html', context)
    def post(self, request):
        pass



### Post list
class PostList(View):
    def get(self, request):
        context = {
            'title' : 'Post list'
        }
        return render(request, 'post/post_list.html', context)
    def post(self, request):
        pass



### Post search
# class PostSearch(View):
#     def get(self, request):
#         context = {
#             'title' : 'Post search'
#         }
#         return render(request, 'post/post_search.html', context)
#     def post(self, request):
#         pass




