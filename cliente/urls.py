from django.urls import path
from .views import export_leads_pdf

urlpatterns = [
    path('leads/pdf/', export_leads_pdf, name='export_leads_pdf'),
]
