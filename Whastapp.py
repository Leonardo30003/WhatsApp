import pywhatkit
import pyautogui as spam
import time

"""numero = input("Ingrse el numero al que le quiere enviar el mensaje")"""
mensaje = input("Ingrese el mensaje que quiere enviar ")
numeroMensajes = input("Numero de veces para enviar el mensaje")
"enviar mensaje a la hora deseada"
"""pywhatkit.sendwhatmsg(numero, mensaje, 10, 39)
"""
"""abrir videos de YouTube
pywhatkit.playonyt("Ylvis - The Fox (What Does The Fox Say?) [Official music video HD]")"""

#############################################################################################
#############################################################################################
""""para utilizar estas lineas de codigo debe tener abierto el whatsaap web abierto y al ejecutar dar enter
pero debe ponerse en comentario el codigo de enviar mensajes a la hora deseada"""

#enviar spam de mensajes
i = 0
time.sleep(5)
while i < int(numeroMensajes):
    spam.typewrite(mensaje)
    spam.press("enter")
    i += 1
    print("enviado")

