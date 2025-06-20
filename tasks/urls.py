from django.urls import path
from . import views
urlpatterns=[
    path('',views.home_view,name='home'),
    path('create-task',views.create_task_view,name='create'),
    path('update-task/<int:pk>',views.update_task_view,name='update'),
    path('delete-task/<int:pk>',views.delete_task_view,name='delete'),
]