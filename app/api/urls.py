from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'order', OrderViewSet)
router.register(r'custom-order', CustomOrderViewSet)
router.register(r'orderdetail', OrderDetailViewSet)

urlpatterns = router.urls
