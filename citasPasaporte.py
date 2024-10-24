import requests
import json
from twocaptcha import TwoCaptcha
import time
import config
import smtplib, ssl


# Definitions
solver = TwoCaptcha(config.TwoCaptchaAPI)
dni = config.dni
sedes = config.sedes
port = config.port
smtp_server = config.smtp_server
sender_email = config.sender_email
receiver_email = config.receiver_email
password = config.password
reporte = "Subject: Citas disponibles para obtener pasaporte.\n\n"


# Variables
disponibilidad = 0


# Functions
def send_api_request(apiurl, data):
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'es-419,es;q=0.9,en;q=0.8,pt;q=0.7',
        'origin': 'https://citaspasaporte.migraciones.gob.pe',
        'priority': 'u=1, i',
        'referer': 'https://citaspasaporte.migraciones.gob.pe/citas-pasaporte-v2/programar-cita',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }
    response = requests.post(apiurl, json=data, headers=headers)
    return response

def ReCaptchaSolver():
    result = solver.recaptcha(
        sitekey='6LeCYTglAAAAALS6ORUZpOI4AwbX0NfLgesYY-FZ',
        url='https://citaspasaporte.migraciones.gob.pe/citas-pasaporte-v2/programar-cita')
    return result['code']

def EmailReport():
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, reporte)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 

if __name__ == "__main__":

    for sede in sedes:
        CaptchaResult = ReCaptchaSolver()

        apiurl = "https://citaspasaporte.migraciones.gob.pe/citas-backend/dependencia/validar-disponibilidad" 
        data = {
            "sid":sede,
            "sCaptcha": CaptchaResult,
            "numeroDni":dni
            }
        
        response = send_api_request(apiurl, data)

        print(f"Sede: {response.json()['data']['sNombre']}")
        print(response.json()['mensaje'])
        print(f"Cupos: {response.json()['data']['cupos']}\n")
        reporte = reporte + f"Sede: {response.json()['data']['sNombre']}\n"
        reporte = reporte + response.json()['mensaje'] + "\n"
        reporte = reporte + f"Cupos: {response.json()['data']['cupos']}\n\n"

        if response.json()['data']['cupos'] > 0:
            disponibilidad = disponibilidad + 1

    if disponibilidad > 0:
        print(f"Hay disponibilidad en {disponibilidad} sede(s)" )
        print("Enviando correo...")
        EmailReport()
        input("Press Enter to exit...")
    else:
        print("No hay disponibilidad, cerrando en 5 segundos")
        segundos = 5
        while segundos > 0:
            print(segundos, end="...\r")
            time.sleep(1)
            segundos -= 1
        print("Adios")



