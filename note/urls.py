from rest_framework import routers

from note.viewsets import NoteViewSet

router = routers.SimpleRouter()
router.register('', NoteViewSet)

urlpatterns = router.urls