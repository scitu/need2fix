from django.core.exceptions import ValidationError, PermissionDenied
from rest_framework import serializers
from app.models import Task
from app.util import is_mechanic, is_mechanic_above

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'create_date', 'done_date', 'requester', )

    def create(self, validated_data):
        user = self.context['request'].user
        if user:
            validated_data['status'] = '1'
            validated_data['requester'] = user
            try:
                return Task.objects.create(**validated_data)
            except ValidationError as err:
                raise err

    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.status == '3':
            raise Exception("Can't modify Done task")
        if (instance.operator and is_mechanic(user) and instance.operator==user)\
                or user.is_superuser:
            return super(TaskSerializer, self).update(instance, validated_data)
        else:
            raise PermissionDenied()

#     def save_form_data(self, instance, validated_data):
#         if validated_data and validated_data[0]: # Replace file
# #            self.delete_file(instance)
#             super(RemovableFileField, self).save_form_data(instance, validated_data[0])
#         if validated_data and validated_data[1]: # Delete file
#             self.delete_file(instance)
#             setattr(instance, self.name, None)

# class TaskChangeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
