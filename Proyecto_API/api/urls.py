from django.urls import path
from .views import CompanyView

urlpatterns = [
    # Define URL patterns for the CompanyView
    path('companies/', CompanyView.as_view(), name='company-list'),
    path('companies/<int:id>/', CompanyView.as_view(), name='company-detail'),
    path('companies/update/<int:id>', CompanyView.as_view(), name='company-update'),
    path('companies/delete/<int:id>', CompanyView.as_view(), name='company-delete'),
]