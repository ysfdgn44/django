from django.urls import path
from .views import home, student_list,student_list_creat,student_detail_update_delete, student_create,student_detail, student_update, student_delete




urlpatterns = [
    path('', home),
    path('student_list/', student_list),
    path('student_list_creat/', student_list_creat),
    path('student_create/', student_create),
    path('student_detail/<int:pk>', student_detail),
    path('student_update/<int:pk>', student_update),
    path('student_delete/<int:pk>', student_delete),
    path('student_detail_update_delete/<int:pk>', student_detail_update_delete),
 
]
