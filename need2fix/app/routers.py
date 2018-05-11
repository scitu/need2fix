from rest_framework import routers
from app.viewsets import TaskViewSet, BuildingInfoViewSet, DivisionViewSet, MechanicViewSet
router = routers.DefaultRouter()
router.register(r'task', TaskViewSet)
router.register(r'building-info', BuildingInfoViewSet, base_name='building-info')
router.register(r'division-list', DivisionViewSet, base_name='division-list')
router.register(r'mechanic-list', MechanicViewSet, base_name='mechanic-list')