from rest_framework import routers
from .api import CabViewSet

router = routers.DefaultRouter()
router.register('api/cab', CabViewSet, 'cab')

urlpatterns = router.urls