from django.shortcuts import render
from .models import  Course
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer  import CourseSerializer
from rest_framework import status

@api_view(['GET','POST'])  # using @api_view for UI
def courseview(request):
    if request.method=='GET':
        course=Course.objects.all()
        serializer=CourseSerializer(course, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
 
@api_view(['PUT','DELETE','GET'])
def Coursedetailview(request,pk):
    try:
        course=Course.objects.get(pk=pk)
    except course.DoesNotExist:
        return Response(status=404)

    if request.method =='PUT':
        serializer=CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    elif request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

    elif request.method=='GET':
        serializer=CourseSerializer(course)
        return Response(serializer.data)