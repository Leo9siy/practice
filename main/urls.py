from django.urls import path

from main.views import TaskListView, TagListView, TagDeleteView, TagUpdateView, TaskUpdateView, TaskDeleteView, \
    TaskCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task_update"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),

    path("tags/", TagListView.as_view(), name="tags_list"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag_update"),
]

app_name = 'main'
