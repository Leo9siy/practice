from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from main import forms
from main.models import Task, Tag


class TaskListView(ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = "task/tasks.html"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            task = Task.objects.get(pk=request.POST['id'])
            task.done = not task.done
            task.save()
            return redirect(reverse_lazy('main:task_list'))


class TaskCreateView(CreateView):
    model = Task
    context_object_name = 'task_create'
    template_name = "task/task_create.html"
    form_class = forms.TaskCreateForm
    success_url = reverse_lazy('main:task_list')


class TaskUpdateView(UpdateView):
    model = Task
    context_object_name = 'task'
    template_name = "task/task_update.html"
    fields = '__all__'


class TaskDeleteView(DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = "task/task_delete.html"
    success_url = reverse_lazy('main:task_list')


class TagCreateView(CreateView):
    model = Tag
    context_object_name = 'tag'
    template_name = "tag/tag_create.html"


class TagListView(ListView):
    model = Tag
    context_object_name = 'tags_list'
    template_name = "task/tags.html"


class TagUpdateView(UpdateView):
    model = Tag
    context_object_name = 'tag'
    template_name = "tag/tag_update.html"
    fields = '__all__'


class TagDeleteView(DeleteView):
    model = Tag
    context_object_name = 'tag'
    template_name = "tag/tag_delete.html"
    fields = '__all__'