from django.contrib import admin
from django.http import HttpResponse
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

from .models import Lead
from .utils.excel import exportar_leads_excel


# -------------------------------------------------------------------
# PDF 1: CONTACTO (ligero, para venta rápida)
# -------------------------------------------------------------------
def exportar_contactos_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        'attachment; filename="leads_contacto.pdf"'
    )

    doc = SimpleDocTemplate(
        response,
        pagesize=landscape(A4),
        rightMargin=20,
        leftMargin=20,
        topMargin=20,
        bottomMargin=20,
    )

    styles = getSampleStyleSheet()
    elementos = []

    elementos.append(Paragraph("LISTADO DE CONTACTOS", styles["Title"]))
    elementos.append(Spacer(1, 12))

    tabla_data = [
        ["Nombre", "Teléfono", "Email", "Ciudad", "Estado"]
    ]

    for lead in queryset:
        tabla_data.append([
            lead.nombre,
            lead.telefono,
            lead.email,
            lead.ciudad,
            lead.estado,
        ])

    tabla = Table(tabla_data, repeatRows=1)
    tabla.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONT", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN", (1, 1), (-1, -1), "LEFT"),
    ]))

    elementos.append(tabla)
    doc.build(elementos)
    return response


# -------------------------------------------------------------------
# PDF 2: FICHA COMPLETA DEL CLIENTE
# -------------------------------------------------------------------
def exportar_ficha_cliente_pdf(modeladmin, request, queryset):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = (
        'attachment; filename="leads_ficha_cliente.pdf"'
    )

    doc = SimpleDocTemplate(
        response,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30,
    )

    styles = getSampleStyleSheet()
    elementos = []

    elementos.append(Paragraph("FICHA COMPLETA DEL CLIENTE", styles["Title"]))
    elementos.append(Spacer(1, 15))

    for lead in queryset:
        datos = [
            ["Nombre", lead.nombre],
            ["Teléfono", lead.telefono],
            ["Email", lead.email],
            ["Ciudad", lead.ciudad],
            ["Estado", lead.estado],
            ["Tipo de financiamiento", lead.tipo_financiamiento],
            ["Valor del bien", lead.valor_bien],
            ["Entrada", lead.entrada],
            ["Plazo (meses)", lead.plazo_meses],
            ["Ingreso mensual", lead.ingreso_mensual],
            ["Tipo de empleo", lead.tipo_empleo],
            ["Tiempo empleo (meses)", lead.tiempo_empleo_meses],
            ["Fecha de creación", lead.creado_en.strftime("%d/%m/%Y %H:%M")],
        ]

        tabla = Table(datos, colWidths=[180, 300])
        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (0, -1), colors.whitesmoke),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
            ("FONT", (0, 0), (0, -1), "Helvetica-Bold"),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))

        elementos.append(tabla)
        elementos.append(Spacer(1, 20))

    doc.build(elementos)
    return response


# -------------------------------------------------------------------
# ADMIN
# -------------------------------------------------------------------
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "telefono",
        "email",
        "ciudad",
        "estado",
        "tipo_financiamiento",
        "valor_bien",
        "creado_en",
    )

    list_filter = (
        "estado",
        "ciudad",
        "tipo_financiamiento",
        "consentimiento",
    )

    search_fields = (
        "nombre",
        "telefono",
        "email",
    )

    readonly_fields = (
        "creado_en",
        "fecha_consentimiento",
        "politica_version",
    )

    actions = [
        exportar_contactos_pdf,
        exportar_ficha_cliente_pdf,
        exportar_leads_excel,
    ]

    exportar_contactos_pdf.short_description = (
        "Exportar contactos (PDF)"
    )
    exportar_ficha_cliente_pdf.short_description = (
        "Exportar ficha completa (PDF)"
    )
    exportar_leads_excel.short_description = (
        "Exportar Leads a Excel"
    )
