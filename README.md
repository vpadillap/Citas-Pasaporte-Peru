# Citas Pasaporte Perú 🇵🇪

Este script en Python te ayuda a encontrar citas disponibles para obtener tu pasaporte en las oficinas de Migraciones Perú. ¡Verifica automáticamente si existen citas disponibles y te envía una notificación por correo electrónico cuando encuentra citas!

¿Cansado de actualizar constantemente el sitio web de Migraciones? ¡Deja que este script haga el trabajo por ti!


## Características

* **Verificación Automatizada de Citas:** El script consulta regularmente la API de Migraciones para verificar la disponibilidad de citas para el pasaporte.
* **Notificaciones por Correo Electrónico:** Recibe alertas instantáneas por correo electrónico cuando las citas estén disponibles en tus sedes escogidas.
* **Configuración Personalizable:** Configura fácilmente el script para monitorear oficinas específicas de Migraciones (sedes) y establece tus preferencias de notificación.
* **Resolución de Captcha:** Utiliza la API de 2Captcha para evitar los desafíos de reCAPTCHA.


## Requisitos

* **Python 3.x:** Descarga e instala la última versión de Python desde [https://www.python.org/](https://www.python.org/).

* **Librerías de Python Requeridas:**

    ```
    requests
    twocaptcha
    smtplib
    ssl
    json
    time
    ```

    Puedes instalar estas bibliotecas usando pip:

    ```bash
    pip install requests twocaptcha smtplib ssl json time
    ```

* **Cuenta 2Captcha:** Regístrate para obtener una cuenta gratuita en [https://2captcha.com/](https://2captcha.com/) y obtén tu clave API.


## Configuración

### Obtén tu Clave API de 2Captcha:

1. Visita [https://2captcha.com/](https://2captcha.com/) y regístrate para obtener una cuenta.
2. Navega a la configuración de tu cuenta y obtén tu clave API.


### Actualiza `config.py`:

1. Abre el archivo `config.py` y reemplaza los valores de los marcadores de posición con tu información:
    * `TwoCaptchaAPI`: Pega tu clave API de 2Captcha aquí.
    * `dni`: Ingresa tu número de DNI.
    * `sedes`: Especifica los códigos de las oficinas de Migraciones (ej: "BLV", "25") que deseas monitorear.
    * `sender_email`: Tu dirección de correo electrónico. Puedes crear una nueva cuenta en cualquier servicio que permita el envío por smtp como gmail y habilitar el acceso smtp, de ese modo no expones las credenciales de tu correo personal.
    * `receiver_email`: La dirección de correo electrónico donde deseas recibir las notificaciones.
    * `password`: Tu contraseña del correo electrónico que se usará para enviar las notificaciones.



## Cómo Ejecutar

1. **Guarda el Script:** Descarga o clona este repositorio en tu computadora.

2. **Navega al Directorio:** Abre tu terminal o símbolo del sistema y navega al directorio donde guardaste el script.

3. **Ejecuta el Script:** Ejecuta el siguiente comando:

    ```bash
    python citasPasaporte.py
    ```

4. **Prográmalo:** Puedes utilizar el método de tu preferencia para programar la ejecución del script en momentos determinados, sea con la programación de tareas de Windows o con un crontab en Linux, de modo que el script se ejecute a una hora determinada todos los días.


## Descargo de Responsabilidad

Este script se proporciona "tal cual" sin garantía de ningún tipo, expresa o implícita. Úsalo bajo tu propio riesgo. El desarrollador no se responsabiliza de ningún problema o consecuencia que surja del uso de este script.