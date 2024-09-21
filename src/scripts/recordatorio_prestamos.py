import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from datetime import datetime, timedelta
import logging
import argparse
import ssl

# configurar el logging
log_file = '/home/gera/Develop/CursoPython/curso_python/src/scripts/recordatorio_prestamos.log'
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuración del correo
SMTP_SERVER = 'mail.fortesitio.com'
SMTP_PORT = 465  # Cambiamos el puerto a 465
SMTP_USERNAME = 'gerardo@fortesitio.com'
SMTP_PASSWORD = 'Muymuysecreto#0'

DB_PATH = '/home/gera/Develop/CursoPython/curso_python/src/biblioteca/db.sqlite3'

def enviar_correo(destinatario, asunto, cuerpo):
    try:
        mensaje = MIMEMultipart()
        mensaje['From'] = SMTP_USERNAME
        mensaje['To'] = destinatario
        mensaje['Subject'] = asunto
        mensaje.attach(MIMEText(cuerpo, 'plain'))

        # Creamos un contexto SSL
        context = ssl.create_default_context()

        # Usamos SMTP_SSL en lugar de SMTP
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
            server.login(SMTP_USERNAME, SMTP_PASSWORD)
            server.send_message(mensaje)
        
        logging.info(f"Correo enviado a {destinatario}")
    except Exception as e:
        logging.error(f"Error al enviar correo a {destinatario}: {str(e)}")

def obtener_prestamos_por_vencer(dias):
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        fecha_limite = (datetime.now() + timedelta(days=dias)).date()
        
        query = """
        SELECT p.id, u.email, l.titulo, p.fecha_devolucion
        FROM prestamos_prestamo p
        JOIN auth_user u ON p.usuario_id = u.id
        JOIN libros_libro l ON p.libro_id = l.id
        WHERE p.fecha_devolucion <= ? AND p.status = 'prestado'
        """
        
        cursor.execute(query, (fecha_limite,))
        prestamos = cursor.fetchall()
        
        cursor.close()
        conn.close()
        
        return prestamos
    except Exception as e:
        logging.error(f"Error al obtener préstamos: {str(e)}")
        return []
    
def main(dias):
    logging.info(f"Iniciando proceso de envío de recordatorios para préstamos que vencen en {dias} días")
    
    prestamos = obtener_prestamos_por_vencer(dias)
    
    for prestamo in prestamos:
        asunto = "Recordatorio: Devolución de libro"
        cuerpo = f"""
        Estimado usuario,

        Le recordamos que el libro "{prestamo['titulo']}" debe ser devuelto el {prestamo['fecha_devolucion']}.

        Por favor, asegúrese de devolverlo a tiempo para evitar sanciones.

        Gracias por su atención.

        Biblioteca
        """
        
        enviar_correo(prestamo['email'], asunto, cuerpo)
    
    logging.info(f"Proceso finalizado. Se enviaron {len(prestamos)} recordatorios.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Envía recordatorios de devolución de libros.'
    )
    parser.add_argument(
        'dias', type=int, help='Número de días antes del vencimiento para enviar el recordatorio')
    args = parser.parse_args()
    
    main(args.dias)


# Cron, es el programador de tareas de linux ( unix )
# para programar tareas usar el comando: crontab -e
'''
 * * * * * <command to execute>
 | | | | |
 | | | | day of the week (0-6) (Sunday to Saturday; 
 | | | month (1-12)             7 is also Sunday on some systems)
 | | day of the month (1-31)
 | hour (0-23)
 minute (0-59)

0 8 * * * python3 /home/gera/Develop/Curso_python/curso_python/lambdas/recordatorio_prestamos.py 10
* * * * * (cada minuto)
'''