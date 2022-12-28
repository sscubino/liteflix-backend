from movies.views import BackdropImageViewSet, MoviesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', MoviesViewSet, basename='')
router.register(r'images', BackdropImageViewSet, basename='image')
urlpatterns = router.urls
