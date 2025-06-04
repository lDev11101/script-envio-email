from email_with_docs import enviar_correo_con_adjuntos

destinatario = input("Correo destinatario: ")
mensaje = input("Mensaje: ")
asunto = input("Asunto: ")
archivos = input("Rutas de archivos separados por coma: ").split(",")

# Elimina espacios en blanco
archivos = [a.strip() for a in archivos if a.strip()]

enviar_correo_con_adjuntos(destinatario, mensaje, asunto, archivos)
