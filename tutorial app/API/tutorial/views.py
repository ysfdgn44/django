from django.shortcuts import render
from .serializer import Tutorial, TutorialSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
 

# Create your views here.
class TutorialViev(ModelViewSet):
    queryset = Tutorial.objects.all()
    serializer_class = TutorialSerializer

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response({'data':serializer.data, 'message':'Succesfully created!'}, status=status.HTTP_201_CREATED, headers=headers)

    # def perform_create(self, serializer):
    #     serializer.save()
