

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
   path('auth/', include('dj_rest_auth.urls'))
]

#--Rooter---------------
from rest_framework.routers import DefaultRouter
from .views import UserView
router = DefaultRouter()
router.register('', UserView)
urlpatterns += router.urls
