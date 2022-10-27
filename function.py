from re import X
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from pyautogui import sleep
import pyautogui as pg
import speech_recognition as sr
import pyttsx3
import pywhatkit


from datetime import datetime as dt

salud = [
    "Segun mi informacion debo recordarte",
    "No puedes consumir alimentos",
    "Salados",
    "dulces",
    "Carne roja",
    "Grasas saturadas",
    "Alcool",
    "Grasas Trans"
]

recordatorio = []

def talk(text):
    nanavoice = pyttsx3.init()
    nanavoice.setProperty('rate', 150)
    nanavoice.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
    print(text)
    nanavoice.say(text)
    nanavoice.runAndWait()

def take_command(): # Comando principal
    listener = sr.Recognizer()
    command = ''

    try:
        with sr.Microphone() as source:
            print("Escuchando...")
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)
        if command == "":
            talk("No he escuchado nada, porfavor pulse e intente nuevamente")
    except:
        conmand = "None"

    return command

def run_nana(order):
    now = dt.now()
    if 'reproduce' in order: # optimizar porfavor
        song = order.replace('reproduce', '')
        talk('Reproduciendo ' + song)
        pywhatkit.playonyt(song)
    elif 'mensaje' in order:
        # se debe implementar una opción que deje buscar contactos por nombre, y extraer el número de ahí
        talk('¿Qué quieres decirle?')
        mensaje = take_command()
        # número de angelica como prueba
        pywhatkit.sendwhatmsg_instantly('+584120999401', mensaje, 11, True, 6)
    elif "hoy" in order or "fecha" in order:
        talk(f"Hoy estamos a {now.day} de {now.month} del año {now.year}")
    elif "hora" in order:
        talk(f"Son las {now.hour} horas con {now.minute} minutos")
    elif "recordatorio" in order:
        talk("¿Que desea recordar?")
        mensaje = take_command()
    elif "hipertenso" in order: # Modificar cuando tengamos la BD implementada # ["hipertenso", "hipertensa", "hipertension"]
        talk(f"{salud[0]}{salud[1]}, {salud[2]}, {salud[3]} y {salud[4]}") # https://www.medicalnewstoday.com/articles/es/alimentos-a-evitar-con-presion-arterial-alta#alimentos-salados
    elif  "diabetes" in order: #["diabetes", "diabetico", "diabetica", "diabete"]
        talk(f"{salud[0]}{salud[1]}{salud[3]} y {salud[7]}")


def send_nana(json,persona, mensaje):
    now = dt.now()
    for k,v in json.items():
        if persona == k:
            pywhatkit.sendwhatmsg_instantly(v, mensaje, 20, True, 15)
            pg.press("enter")