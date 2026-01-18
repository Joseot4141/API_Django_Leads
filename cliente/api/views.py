from rest_framework import viewsets, status
from rest_framework.response import Response

from cliente.models import Lead
from .serializers import (
    LeadCreateSerializer,
    LeadListSerializer
)


class LeadViewSet(viewsets.ModelViewSet):
    """
    API para manejar Leads:
    - POST   -> crear lead (Flutter)
    - GET    -> listar / detalle
    - DELETE -> eliminar lead
    """

    queryset = Lead.objects.all().order_by('-creado_en')

    def get_serializer_class(self):
        # POST usa serializer reducido (Flutter)
        if self.action == 'create':
            return LeadCreateSerializer
        # GET usa serializer completo
        return LeadListSerializer

    def create(self, request, *args, **kwargs):
        """
        POST /api/leads/
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        lead = serializer.save()

        return Response(
            {
                "mensaje": "Lead creado correctamente",
                "id": lead.id
            },
            status=status.HTTP_201_CREATED
        )
