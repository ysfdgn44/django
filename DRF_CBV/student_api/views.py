from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

class StudentListCreate(APIView):
    

    #Listele(GET)
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(instance=students, many=True)
        return Response(serializer.data)
    

    #Yeni kayıt(POST)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class StudentDetailUpdateDelete(APIView):
    #tek kayıt görüntüle
    def get(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student)
        return Response(serializer.data)
    

    #tek kayıt güncelle
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #tek kayıt silme
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({'message':'deleted'}, status=status.HTTP_204_NO_CONTENT )
    



# Tüm işlemleri tek class ta birleştirme
class StudentGPPD(APIView):

    def get(self, request, pk=0):
        if pk:
        #tek kayıt görüntüle
            student = get_object_or_404(Student, id=pk)
            serializer = StudentSerializer(instance=student)
            return Response(serializer.data)
        else:
        #çoklu kayıt gösterme
            students = Student.objects.all()
            serializer = StudentSerializer(instance=students, many=True)
            return Response(serializer.data)

    #Yeni kayıt(POST)
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #tek kayıt güncelle
    def put(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        serializer = StudentSerializer(instance=student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #tek kayıt silme
    def delete(self, request, pk):
        student = get_object_or_404(Student, id=pk)
        student.delete()
        return Response({'message':'deleted'}, status=status.HTTP_204_NO_CONTENT )
    


from rest_framework.generics import GenericAPIView
from rest_framework import mixins


class StudentGenericListCreat(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)




from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

#kayıt listeleme ve yeni kayıt
class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
 

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

#Tüm işlemler
class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(methods=['GET'], detail=False)
    def count(self, request):
        return Response({
            'count':Student.objects.count()
        })