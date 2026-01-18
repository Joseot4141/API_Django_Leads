from django.db import models


class Lead(models.Model):

    # =========================
    # DATOS PERSONALES
    # =========================
    nombre = models.CharField(
        max_length=120,
        default="Cliente sin nombre"
    )

    telefono = models.CharField(
        max_length=20,
        default="No informado"
    )

    email = models.EmailField(
        default="sin-email@ejemplo.com"
    )

    ciudad = models.CharField(
        max_length=100,
        default="No informada"
    )

    estado = models.CharField(
        max_length=2,
        default="PR"
    )

    # =========================
    # DATOS DEL FINANCIAMIENTO
    # =========================
    TIPO_FINANCIAMIENTO_CHOICES = [
        ("inmueble", "Inmueble"),
        ("vehiculo", "Vehículo"),
        ("personal", "Crédito personal"),
    ]

    tipo_financiamiento = models.CharField(
        max_length=20,
        choices=TIPO_FINANCIAMIENTO_CHOICES,
        default="inmueble"
    )

    valor_bien = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00
    )

    entrada = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00
    )

    plazo_meses = models.PositiveIntegerField(
        default=360  # estándar inmobiliario
    )

    ingreso_mensual = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0.00
    )

    # =========================
    # PERFIL LABORAL
    # =========================
    TIPO_EMPLEO_CHOICES = [
        ("clt", "CLT"),
        ("autonomo", "Autónomo"),
        ("empresario", "Empresario"),
        ("desempleado", "Desempleado"),
    ]

    tipo_empleo = models.CharField(
        max_length=20,
        choices=TIPO_EMPLEO_CHOICES,
        default="clt"
    )

    tiempo_empleo_meses = models.PositiveIntegerField(
        default=0
    )

    # =========================
    # CONSENTIMIENTO (LGPD)
    # =========================
    consentimiento = models.BooleanField(
        default=False
    )

    fecha_consentimiento = models.DateTimeField(
        null=True,
        blank=True
    )

    politica_version = models.CharField(
        max_length=10,
        default="1.0"
    )

    # =========================
    # METADATOS
    # =========================
    creado_en = models.DateTimeField(
        auto_now_add=True
    )

    actualizado_en = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Leads"
        ordering = ["-creado_en"]

    def __str__(self):
        return f"{self.nombre} - {self.telefono}"
