from rest_framework.routers import DefaultRouter

from offices.views import EmployeeAPIViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'employees', EmployeeAPIViewSet, basename='employee')

urlpatterns += router.urls
