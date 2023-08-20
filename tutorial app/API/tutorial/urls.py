from rest_framework.routers import DefaultRouter
from .views import TutorialViev


router = DefaultRouter()
router.register('tutorials', TutorialViev)

urlpatterns =router.urls