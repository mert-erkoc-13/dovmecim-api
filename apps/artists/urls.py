from rest_framework.routers import DefaultRouter
from .views import ArtistProfileViewSet

router = DefaultRouter()
router.register(r'', ArtistProfileViewSet, basename='artistprofile')
urlpatterns = router.urls