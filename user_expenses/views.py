from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.exceptions import ValidationError
from rest_framework import generics,permissions
from .permissions import IsOwner

# Create your views here.

class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Return only the expenses of the logged-in user
        return Expense.objects.filter(user_name=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user_name field to the logged-in user
        serializer.save(user_name=self.request.user) # Automatically set the user to the authenticated user



class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsOwner]