from rest_framework import serializers
from django.utils import timezone
from cliente.models import Lead


# =========================
# SERIALIZER PARA CREAR LEADS (FLUTTER)
# =========================
class LeadCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = [
            'nombre',
            'telefono',
            'email',
            'ciudad',
            'estado',
            'tipo_financiamiento',
            'valor_bien',
            'entrada',
            'plazo_meses',
            'ingreso_mensual',
            'tipo_empleo',
            'tiempo_empleo_meses',
            'consentimiento',
        ]

        extra_kwargs = {
            'nombre': {'required': False},
            'telefono': {'required': True},
            'email': {'required': False},
            'ciudad': {'required': False},
            'estado': {'required': False},
            'tipo_financiamiento': {'required': False},
            'valor_bien': {'required': False},
            'entrada': {'required': False},
            'plazo_meses': {'required': False},
            'ingreso_mensual': {'required': False},
            'tipo_empleo': {'required': False},
            'tiempo_empleo_meses': {'required': False},
        }

    # -------------------------
    # VALIDACIÓN LGPD
    # -------------------------
    def validate_consentimiento(self, value):
        if value is not True:
            raise serializers.ValidationError(
                "El consentimiento es obligatorio para continuar."
            )
        return value

    # -------------------------
    # CREACIÓN DEL LEAD
    # -------------------------
    def create(self, validated_data):
        validated_data['fecha_consentimiento'] = timezone.now()
        validated_data['politica_version'] = "1.0"
        return super().create(validated_data)


# =========================
# SERIALIZER PARA LISTAR LEADS (ADMIN / GET)
# =========================
class LeadListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = '__all__'
