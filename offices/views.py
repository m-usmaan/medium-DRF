from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from offices.models import Employee
from offices.serializers import EmployeeSerializer


class EmployeeAPIViewSet(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        req_user = self.request.user
        return Employee.objects.filter(
            department_id=req_user.department_id
        )