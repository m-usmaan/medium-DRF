from rest_framework.serializers import ModelSerializer
from offices.models import Employee

class EmployeeSerializer(ModelSerializer):
    
    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True},
            'department': {'required': True}
        }
