from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from .models import Todo
from .forms import TodoForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy



class IndexView(ListView):
    template_name = 'todo/index.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.all()

class CreateView(CreateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/new.html'

    def get_success_url(self):
        return reverse('todo:index')


class DetailView(DetailView):
    model = Todo
    template_name = 'todo/detail.html'

class UpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todo/edit.html'

    def get_success_url(self):
        return reverse('todo:index')

class DeleteView(DeleteView):
    model = Todo
    template_name = 'todo/delete.html'
    success_url = reverse_lazy('todo:index')

