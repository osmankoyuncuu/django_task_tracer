from django.urls import path
from .views import (
  task_tracker_list_create, 
  task_tracker_detail
  )


urlpatterns = [
  path('list-create/', task_tracker_list_create),
  path('detail/<int:id>/', task_tracker_detail)
]
