from rest_framework import routers
from .api import NoteViewSet

router = routers.DefaultRouter()
router.register('api/note', NoteViewSet, 'note')

urlpatterns = router.urls