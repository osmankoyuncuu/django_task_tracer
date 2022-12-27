from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Task_Tracker
from .serializers import Task_TrackerSerializer

@api_view(['GET', 'POST'])
def task_tracker_list_create(request):
  if request.method == 'GET':
      task = Task_Tracker.objects.filter(is_done=False)  # is_done false ones to filters
      serializer = Task_TrackerSerializer(task, many=True)
      return Response(serializer.data)
    
  if request.method == 'POST':
      serializer = Task_TrackerSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
        
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
@api_view(['GET', 'DELETE', 'PUT'])
def task_tracker_detail(request, id):
  task = get_object_or_404(Task_Tracker, id=id)
  if request.method == 'GET':
      serializer = Task_TrackerSerializer(task)
      return Response(serializer.data)
    
  if request.method == 'PUT':
      serializer = Task_TrackerSerializer(data=request.data, instance=task)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  if request.method == 'DELETE':
      task.delete()
      return Response({'message': 'task deleted successfully'})
      


