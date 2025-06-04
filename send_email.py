from email.message import EmailMessage
import os
from dotenv import load_dotenv
import smtplib
import ssl


def enviar_correo(destinatario, mensaje):
    # Cargar variables de entorno
    load_dotenv()
    remitente = os.getenv("EMAIL_USER")
    password = os.getenv("PASSWORD")

    if not remitente or not password or not destinatario:
        raise ValueError(
            "Faltan variables de entorno necesarias: EMAIL_USER, PASSWORD o EMAIL_DESTINO."
        )

    # Crear el mensaje de correo
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = "Prueba de envío de correo"
    email.set_content(mensaje)

    # Crear contexto SSL seguro
    context = ssl.create_default_context()
    context.check_hostname = False

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(remitente, password)
            smtp.send_message(email)
        print("Correo enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
