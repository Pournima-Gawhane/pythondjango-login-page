from rest_framework import serializers
from .models import User_detail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields =(
            'id',
            'fullname',
            'email',
            'password',
            'gender',
            'height',
            'weight'
        )
        model=User_detail
