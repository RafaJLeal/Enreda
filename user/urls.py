from rest_framework import routers

from user.viewsets import UserViewSet

router = routers.SimpleRouter()
router.register('', UserViewSet)

urlpatterns = router.urls