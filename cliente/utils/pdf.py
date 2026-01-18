from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


def pdf_leads_contacto(response, queryset):
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    y = height - 50
    p.setFont("Helvetica-Bold", 14)
    p.drawString(50, y, "LISTADO DE LEADS - CONTACTO")
    y -= 30

    p.setFont("Helvetica", 9)
    p.drawString(50, y, "Nombre")
    p.drawString(180, y, "Teléfono")
    p.drawString(300, y, "Email")
    p.drawString(460, y, "Ciudad/Estado")
    y -= 15

    for lead in queryset:
        if y < 50:
            p.showPage()
            y = height - 50

        p.drawString(50, y, lead.nombre[:25])
        p.drawString(180, y, lead.telefono)
        p.drawString(300, y, lead.email[:30])
        p.drawString(460, y, f"{lead.ciudad}/{lead.estado}")
        y -= 15

    p.save()
    
    
    
    
def pdf_ficha_cliente(response, queryset):
    p = canvas.Canvas(response, pagesize=A4)
    width, height = A4

    for lead in queryset:
        y = height - 50
        p.setFont("Helvetica-Bold", 14)
        p.drawString(50, y, "FICHA DEL CLIENTE")
        y -= 30

        p.setFont("Helvetica", 10)
        campos = [
            ("Nombre", lead.nombre),
            ("Teléfono", lead.telefono),
            ("Email", lead.email),
            ("Ciudad", lead.ciudad),
            ("Estado", lead.estado),
            ("Tipo financiamiento", lead.tipo_financiamiento),
            ("Valor del bien", lead.valor_bien),
            ("Entrada", lead.entrada),
            ("Plazo (meses)", lead.plazo_meses),
            ("Ingreso mensual", lead.ingreso_mensual),
            ("Tipo empleo", lead.tipo_empleo),
            ("Tiempo empleo (meses)", lead.tiempo_empleo_meses),
        ]

        for label, value in campos:
            p.drawString(50, y, f"{label}:")
            p.drawString(200, y, str(value))
            y -= 18

        p.showPage()

    p.save()
