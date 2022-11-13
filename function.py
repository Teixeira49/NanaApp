from re import X
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#from kivy.garden.notification import Notification
from googlesearch import search
import webbrowser

import pyautogui as pg
import speech_recognition as sr
import pyttsx3
import pywhatkit
import random
import requests
import json
from datetime import datetime as dt

with open('data_talk.json', 'r') as file:
    data = json.load(file)


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

'''def notify():
        Notification().open(
            title="Recordatorio",
            icon="./Images/logo blanco.png",
            message="Los granos integrales son preferibles a los productos de harina blanca o pasta para la hipertensión",
            timeout=5,
        )'''

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

    if 'reproduce' in order.lower(): # optimizar porfavor
        song = order.replace('reproduce', '')
        talk('Reproduciendo ' + song)
        pywhatkit.playonyt(song)

    elif 'mensaje' in order.lower():
        # se debe implementar una opción que deje buscar contactos por nombre, y extraer el número de ahí
        talk('¿Qué quieres decirle?')
        mensaje = take_command()
        # número de angelica como prueba
        pywhatkit.sendwhatmsg_instantly('+584120999401', mensaje, 11, True, 6)

    elif "hoy" in order or "fecha" in order.lower():
        talk(f"Hoy estamos a {now.day} de {now.month} del año {now.year}")

    elif "hora" in order.lower():
        talk(f"Son las {now.hour} horas con {now.minute} minutos")

    elif "recordatorio" in order.lower():
        talk("¿Que desea recordar?")
        mensaje = take_command()

    elif "hipertenso" in order.lower(): # Modificar cuando tengamos la BD implementada # ["hipertenso", "hipertensa", "hipertension"]
        #notify()
        talk(f"{salud[0]}{salud[1]}, {salud[2]}, {salud[3]} y {salud[4]}") # https://www.medicalnewstoday.com/articles/es/alimentos-a-evitar-con-presion-arterial-alta#alimentos-salados

    elif  "diabetes" in order: #["diabetes", "diabetico", "diabetica", "diabete"]
        talk(f"{salud[0]}{salud[1]}{salud[3]} y {salud[7]}")
    elif "clima" in order.lower() or "tiempo" in order.lower():
        dat = ""
        if "en " in order:
            dat = "London" # por ahora
        else:
            dat = "Caracas"
        weather(data["weathers"]["urls"]["weather"], data["weathers"]["urls"]["location"], dat, data["weathers"]["key"])
    else:
        talk("De " + order + " " + data["result"][random.randint(0, len(data["result"])-1)])
        lista = search(order)
        valor = ""
        for i in lista:
            if valor == "":
                valor = i
                break
        # Se han encontrado los siguientes resultados print()
        webbrowser.open_new_tab(valor)

def weather(url_t, url_loc, city, key):
    try:
        response = requests.request("GET", (url_loc.replace("city_name", city).replace("limit_d", "1").replace("appid_r", key)))
        lat, lon = response.json()[-1]["lat"], response.json()[-1]["lon"]
        responses = requests.request("GET", (url_t.replace("lat_r", f"{lat}").replace("lon_r", f"{lon}").replace("appid_r", key)))
        x = responses.json()
        clima = x["weather"][0]["main"]
        desc = x["weather"][0]["description"]
        temp = x["main"]["temp"]
        humb = x["main"]["humidity"]
        v_sp = x["wind"]["speed"]
        direc = x["wind"]["deg"]
        numb = x["clouds"]["all"]
        # CONVERTIR EN NOTIFICACION
        talk(f"Clima: {clima}, Descripcion: {desc}, Temperatura promedio: {temp}C°, Humedad: {humb}, viento a velocidad de: {v_sp} sopla en direccion de {direc} con nubosidad de {numb} puntos")
    except:
        print("Error de busqueda")
        weather(url_t, url_loc, "Caracas", key)

def send_nana(json,persona, mensaje):
    now = dt.now()
    for k,v in json.items():
        if persona == k:
            pywhatkit.sendwhatmsg_instantly(v, mensaje, 30, True, 22)
            pg.press("enter")

# PROXIMAMENTE
def repeat():
    pass

def hello():
    pass

def chiste():
    pass

def dayword(): # http://palabras-aleatorias-public-api.herokuapp.com/
    pass

def amen(): # https://es.aleteia.org/2019/12/04/el-ano-liturgico-y-sus-3-ciclos-como-saber-si-es-a-b-o-c/
    pass    # https://scripture.api.bible/

def help():
    pass

def traduct(): # https://www.ibidemgroup.com/edu/traduccion-automatica-texto-python/
    pass
def conf():
    pass
#https://programandofacilsite.wordpress.com/2017/04/23/como-hacer-llamadas-telefonicas-en-python/
# PROXIMAMENTE
# https://ernestocrespo13.wordpress.com/2011/08/15/manejando-contactos-y-realizando-una-llamada-con-python-en-android/
# // https://www.businessinsider.es/chistes-malos-cortos-1043053

#weather(data["weathers"]["urls"]["weather"], data["weathers"]["urls"]["location"], "Caracas", data["weathers"]["key"])