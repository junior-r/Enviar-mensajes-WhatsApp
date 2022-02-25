# pip install pywhatkit
# pip install Flask
# Debes instalar estas dos librerías para que funcione el proyecto.
import pywhatkit 
import datetime

now = datetime.datetime.now()
hour = now.hour
minute = int(now.minute)

enviar_otro = 'si'

def datos():
	number = input('Ingrese número de Teléfono destino: ')
	cero = number[0]
	msg = input('Escriba su mensaje: ')
	if cero == '0':
		# Cambiar el Código de País según tu país.
		# Esto reemplazará el primer caracter del número de telefono introducido, por el código país.
		# Si no quieres que pase, borra: variable -> cero, condicional -> if, number.replace()
		number = number.replace(cero, '+58', 1)
	return number, msg

def send_message(number, msg):
	try:
		pywhatkit.sendwhatmsg_instantly(number, msg, 5)
		print(f'Mensaje Enviado -> {number} Hora -> {hour}:{minute}')
	except Exception as e:
		print('No se pudo Enviar el Mensaje')
		print(e)		

while enviar_otro == 'si':
	number, msg = datos()
	send_message(number, msg)
	enviar_otro = input('¿Desea enviar otro mensaje?: ')
	enviar_otro = enviar_otro.lower()