from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Student
from django.shortcuts import get_object_or_404


@api_view()
def home(request):
    return Response(
        {
            'message':'Hello World'
        }
    )
from .models import Student
from .serializers import StudentSerializer


@api_view(['GET'])  #default GET tir
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    # print(dir(serializer))
    # print((serializer.data))
    return Response(serializer.data)

@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Created Successfully'},status = status.HTTP_201_CREATED)
    else:
        return Response({
            'message':'Data not valid',
            'data':serializer.data
        }, status = status.HTTP_400_BAD_REQUEST)
    



@api_view(['GET'])
def student_detail(request, pk):
    # student = Student.objects.get(id=pk)
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student)
    return Response(serializer.data)


@api_view(['PUT'])
def student_update(request,pk):
    student = get_object_or_404(Student, id=pk)
    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message':'Updated Successfully'},status = status.HTTP_202_ACCEPTED)
    else:
        return Response({
            'message':'Data not valid',
            'data':serializer.data
        }, status = status.HTTP_400_BAD_REQUEST)
    


@api_view(['DELETE'])
def student_delete(request, pk):
    student = get_object_or_404(Student, id=pk)
    student.delete()
    return Response({'message':'Deleted Successfully'},status = status.HTTP_204_NO_CONTENT)



@api_view(['GET','POST'])
def student_list_creat(request):
    if request.method=='GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    else:
         serializer = StudentSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response({'message':'Created Successfully'},status = status.HTTP_201_CREATED)
         else:
            return Response({
            'message':'Data not valid','data':serializer.data}, status = status.HTTP_400_BAD_REQUEST)
         

@api_view(['GET','PUT','DELETE'])
def student_detail_update_delete(request, pk):

    student = get_object_or_404(Student, id=pk)

    match request.method:
        case 'GET':
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)
        case 'PUT':
            serializer = StudentSerializer(instance=student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Updated Successfully'},status = status.HTTP_202_ACCEPTED)
            else:
                return Response({
                'message':'Data not valid',
                'data':serializer.data
                }, status = status.HTTP_400_BAD_REQUEST)
        case 'DELETE':
            student.delete()
            return Response({'message':'Deleted Successfully'},status = status.HTTP_204_NO_CONTENT)