from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

import re

"""
when inheriting  User from django.contrib.auth.models 
you CAN NOT ADD OTHER FIELDS  apart from those that the User model provides like:

username first_name last_name email is_active date_joined groups user_permissions id 
last_login

when creating a user all these fiels are created 
if you want to save only some fields that you want you can
specify in the fields list the fields you want 


fields = ['email','password',first_name,'last_name']

and in this way only these fields will be saved




"""



class BlogUserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['username','password','email']


    def validate_password(self,value):
        if not re.search(r'[A-Z]',value):
            raise ValidationError(detail='password must contain one upperase')

        if len(value) < 8:
            raise ValidationError(detail='password must be at leat 8 characters')
        if not re.search(r'\d',value):
            raise ValidationError(detail='password must contain at least one number')

        return value
        
    
    def validate(self,value):
         # checking to see if the user enters a name that already exists
        if User.objects.filter(username=value["username"]).exists():
            raise ValidationError(detail='username already exists')

        return value

    def create(self, validated_data):
        
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        
        password = validated_data['password']
        user.set_password(password)  
        user.save()  
        return user  # Return the result of the super method


    