from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from prestamos.models import Prestamo

@shared_task
def enviar_recordatorios():
    hoy = timezone.now().date()
    prestamos_por_vencer = Prestamo.objects.all()# filter(fecha_devolucion__lte=hoy + timezone.timedelta(days=3))#, devuelto=False)
    
    for prestamo in prestamos_por_vencer:
        dias_restantes = (prestamo.fecha_devolucion - hoy).days
        asunto = f"Recordatorio: Devolución de libro en {dias_restantes} días"
        mensaje = f"""
        Estimado/a {prestamo.usuario.username},

        Le recordamos que debe devolver el libro "{prestamo.libro.titulo}" en {dias_restantes} días.
        La fecha de devolución es: {prestamo.fecha_devolucion}.

        Gracias por usar nuestra biblioteca.
        """
        send_mail(
            asunto,
            mensaje,
            'gerardo@fortesitio.com',
            [prestamo.usuario.email],
            fail_silently=False,
            auth_user='gerardo@fortesitio.com',
            auth_password='Muymuysecreto#0'
        )
    
    return f"Se enviaron {prestamos_por_vencer.count()} recordatorios."