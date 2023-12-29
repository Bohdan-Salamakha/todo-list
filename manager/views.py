from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic, View

from .forms import TaskForm
from .models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'manager/task_list.html'
    paginate_by = 4


class TaskCreateView(generic.CreateView):
    model = Task
    success_url = reverse_lazy('manager:task-list')
    form_class = TaskForm


class TaskUpdateView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy('manager:task-list')
    form_class = TaskForm


class TaskUpdateCompletionView(View):
    def get(self, request: HttpRequest, pk: str) -> HttpResponseRedirect:
        task = Task.objects.get(id=pk)
        task.is_completed = not task.is_completed
        task.save()
        return redirect('manager:task-list')

    def post(self, request: HttpRequest, pk: str) -> HttpResponseRedirect:
        task = Task.objects.get(id=pk)
        task.is_completed = request.POST.get('is_completed', not task.is_completed)
        task.save()
        return redirect('manager:task-list')


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy('manager:task-list')


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 4
    template_name = 'manager/tag_list.html'
    context_object_name = 'tag_list'


class TagCreateView(generic.CreateView):
    model = Tag
    fields = '__all__'
    template_name = 'manager/tag_form.html'
    success_url = reverse_lazy('manager:tag-list')


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = '__all__'
    template_name = 'manager/tag_form.html'
    success_url = reverse_lazy('manager:tag-list')


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = 'manager/tag_confirm_delete.html'
    success_url = reverse_lazy('manager:tag-list')
