from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import Lead
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated


from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication
)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def export_leads_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="leads.pdf"'

    p = canvas.Canvas(response)
    p.setFont("Helvetica", 10)

    y = 800
    p.drawString(50, y, "LISTADO DE LEADS")
    y -= 30

    leads = Lead.objects.all().order_by('-creado_en')

    for lead in leads:
        texto = f"{lead.nombre or 'Sin nombre'} | {lead.telefono} | {lead.email or '-'}"
        p.drawString(50, y, texto)
        y -= 20

        if y < 50:
            p.showPage()
            p.setFont("Helvetica", 10)
            y = 800

    p.showPage()
    p.save()

    return response
