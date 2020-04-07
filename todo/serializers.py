from rest_framework import serializers
from todo import models


class UserTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.TodoItem
        fields=('id','profile_id','todo','created_on')
        extra_kwargs={'profile_id':{'read_only':True}}


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.UserProfile
        fields=('id','username','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }
    def create(self,validated_data):
        user=models.UserProfile.objects.create_user(
            username=validated_data['username'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user