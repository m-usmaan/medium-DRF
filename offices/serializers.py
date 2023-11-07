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

    def to_internal_value(self, data):
        new_data = data.copy()
        new_data['department'] = self.context.request.user.department_id
        return super().to_internal_value(new_data)
