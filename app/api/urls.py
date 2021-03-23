from rest_framework import routers
from .viewsets import *


router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'orderdetail', OrderDetailViewSet)

urlpatterns = router.urls
