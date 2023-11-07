from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
    
    # def create(self, request, *args, **kwargs):
    #     new_data = request.data.copy()
    #     new_data['department'] = request.user.department_id  # SEE THIS
    #     serializer = self.get_serializer(data=new_data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)