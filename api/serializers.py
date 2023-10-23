from rest_framework import serializers
from gsd.models import User, Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['id', 'username', 'email']
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    owner = UserSerializer()

    class Meta:
        model = Task
        fields =  ['id', 'name', 'category', 'owner']