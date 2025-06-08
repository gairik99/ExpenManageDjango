from rest_framework import serializers
from .models import Expense

class ExpenseSerializer(serializers.ModelSerializer):
    user_name=serializers.StringRelatedField(read_only=True) 
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['id']  