from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,style={'input_type': 'password'})
    first_name = serializers.CharField(max_length=30, )
    last_name = serializers.CharField(max_length=30,)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name','password2']

        extra_kwargs = {
        'password': {'write_only': True, 'style': {'input_type': 'password'}},  
      }
        
    def validate(self, data):
        # Check if passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})

        # Check if username already exists
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({"username": "Username already exists."})

        # Check if email already exists
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "Email already exists."})

        return data
    
    
    def create(self, validated_data):
        # Remove password2 as it is not part of User model
        validated_data.pop('password2')

        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    # def save(self):
    #     user = User(
    #         username=self.validated_data['username'],
    #         email=self.validated_data['email'],
    #         first_name=self.validated_data['first_name'],
    #         last_name=self.validated_data['last_name']
    #     )
    #     password = self.validated_data['password']
    #     password2 = self.validated_data['password2']
        
    #     if password != password2:
    #         raise serializers.ValidationError("Passwords do not match.")
        
    #     if User.objects.filter(email=self.validated_data['email']).exists():
    #         raise serializers.ValidationError("Email already exists.")
    #     user.set_password(password)
    #     user.save()
    #     return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Add custom user data here
        data.update({
            'user_id': self.user.id,
            'username': self.user.username,
            'email': self.user.email,
            # Add any custom field if required, e.g.
            # 'is_admin': self.user.is_staff,
        })

        return data