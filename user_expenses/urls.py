from .views import ExpenseListCreateView,ExpenseDetailView 
from django.urls import path


urlpatterns = [
    path('listcreate/', ExpenseListCreateView.as_view(), name='expense-list-create'),  
    path('<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'), 
]