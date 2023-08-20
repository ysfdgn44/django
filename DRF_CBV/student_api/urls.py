from django.urls import path
from .views import StudentListCreate, StudentDetailUpdateDelete, StudentGPPD,StudentGenericListCreat, StudentListCreateAPIView



urlpatterns = [
    path('student_list_create/', StudentListCreate.as_view()),
    path('student_detail_update_delete/<int:pk>', StudentDetailUpdateDelete.as_view()),
    path('studentgppd/<int:pk>', StudentGPPD.as_view()),
    path('studentgppd/', StudentGPPD.as_view()),
    path('student_generic_list_creat/', StudentGenericListCreat.as_view()),
    path('student_list_create_apiv/', StudentListCreateAPIView.as_view())
    
]


from .views import StudentMVS
from rest_framework import routers


router = routers.DefaultRouter()
router.register('students', StudentMVS)
urlpatterns += router.urls

