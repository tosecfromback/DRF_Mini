from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.contrib.auth import authenticate

# Create your views here.

### GPT Index
class GPTIndex(View):
    def get(self, request):
        context = {
            'title' : 'GPT Index'
        }
        return render(request, 'gpt/gpt_index.html', context)
    def post(self, request):
        pass
