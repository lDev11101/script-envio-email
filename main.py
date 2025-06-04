from send_email import enviar_correo

destinatario = input("Introduce el correo del destinatario: ")
mensaje = input("Escribe el mensaje a enviar: ")

enviar_correo(destinatario, mensaje)
