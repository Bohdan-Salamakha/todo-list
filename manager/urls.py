from django.urls import path

from manager.views import (
    TaskListView,
    TaskUpdateView,
    TaskUpdateCompletionView,
    TaskCreateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagDeleteView,
    TagUpdateView,
)

urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('<int:pk>/', TaskUpdateCompletionView.as_view(), name='update-completion'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tags/', TagListView.as_view(), name='tag-list'),
    path('tags/create/', TagCreateView.as_view(), name='tag-create'),
    path('tags/<int:pk>/update/', TagUpdateView.as_view(), name='tag-update'),
    path('tags/<int:pk>/delete/', TagDeleteView.as_view(), name='tag-delete'),
]

app_name = 'manager'
