from rest_framework import routers
from web import api_views as views

router = routers.DefaultRouter()
router.register(r'bicycle', views.BicycleViewset)