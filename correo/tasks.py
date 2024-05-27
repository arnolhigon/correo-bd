def sumar_numeros():
    a, b = [5, 3] 
    suma = a + b
    print(f"La suma de {a} y {b} es {suma}")
    return suma


def restar_numeros():
    a, b = [8, 2]  # Valores para la resta
    resta = a - b
    print(f"La resta de {a} y {b} es: {resta}")
    return resta

def multiplicar():
    a, b = [8, 2]  # Valores para la resta
    m = a * b
    print(f"La multiplicacion de {a} y {b} es: {m}")
    return m






import imaplib
import email
from email.header import decode_header, make_header
import io
from django.shortcuts import render
from django.conf import settings
from django.core.files import File
from .models import Email
import logging
from dateutil.parser import parse



def import_emails():

    username = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD
    print(username, password)

    # Conexión al servidor IMAP de Gmail
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)
    mail.select("inbox")

    # Buscar todos los correos en la bandeja de entrada
    status, messages = mail.search(None, "ALL")
    mail_ids = messages[0].split()

    # Procesar cada correo
    for mail_id in mail_ids:
        status, msg_data = mail.fetch(mail_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject, subject_encoding = decode_header(msg["Subject"])[0]
                if subject_encoding:
                    try:
                        subject = subject.decode(subject_encoding)
                    except (LookupError, UnicodeDecodeError):
                        subject = subject.decode('utf-8', 'ignore')
                else:
                    subject = str(make_header(decode_header(msg["Subject"])))

                # Verificar si el asunto ya existe en la base de datos
                if Email.objects.filter(subject=subject).exists():
                    print("ya existe en la base de datos. Saltando...")
                    continue

                sender, sender_encoding = decode_header(msg.get("From"))[0]
                if sender_encoding:
                    try:
                        sender = sender.decode(sender_encoding)
                    except (LookupError, UnicodeDecodeError):
                        sender = sender.decode('utf-8', 'ignore')
                else:
                    sender = str(make_header(decode_header(msg.get("From"))))

                date_str = msg.get("Date")
                date = parse(date_str)

                # Insertar el correo en la base de datos
                zip_file = None
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_maintype() == 'multipart':
                            continue
                        if part.get('Content-Disposition') is None:
                            continue
                        filename = part.get_filename()
                        if filename and filename.endswith('.zip'):
                            content = part.get_payload(decode=True)
                            zip_file = File(io.BytesIO(content), name=filename)
                            break  # Guardar solo el primer archivo .zip encontrado

                # Insertar el correo en la base de datos solo si se encontró un .zip
                if zip_file:
                    Email.objects.create(subject=subject, sender=sender, date=date, zip_file=zip_file)

    # Cerrar la conexión a Gmail
    mail.logout()


