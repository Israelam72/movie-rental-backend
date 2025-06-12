from rest_framework import serializers
from django.contrib.auth.models import User
import re


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        max_length=15,
        error_messages={
            'min_length': 'Password must be at least 8 characters long',
            'max_length': 'Password must be less than 15 characters long',
        }
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already exists')
        return value

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('Email already exists')
        return value

    def validate_password(self, value):
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,15}$'
        if not re.match(pattern, value):
            raise serializers.ValidationError(
                "Password must contain at least one lowercase letter, one uppercase letter, one number, "
                "and be 8-15 characters long, using only letters and numbers."
            )
        return value

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
