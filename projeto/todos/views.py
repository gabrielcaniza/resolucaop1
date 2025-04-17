from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Todo
from django.views.generic import ListView, CreateView

class TodoListView(ListView):
    model=Todo


class TodoCreateView:
    model=Todo
    fields=['title', 'deadline']
    success_url = reverse_lazy('todo_list')
    

# Create your views here.
