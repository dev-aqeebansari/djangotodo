
from django.urls import path
from . import views
urlpatterns=[
    path('addTask/',views.addTask, name="addTask"),
    path('markasdone/<int:pk>/',views.mark_as_done, name="mark_as_done"),
    path('markasundone/<int:pk>/',views.mark_as_undone, name="mark_as_undone"),
    #Edit Task
    path('edit_task/<int:pk>', views.edit_task, name="editTask"),
    #Delete Task
    path('delete_task/<int:pk>', views.delete_task, name="delete_task"),
]