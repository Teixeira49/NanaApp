# =========================================================================================================
from re import X
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from plyer import notification
#from googlesearch import search
from googlesearch.googlesearch import GoogleSearch #para solucionar el error de search en mi compubrew install portaudiobrew install portaudio
import webbrowser
# ============================================================================== Librerias Kivy ===========
import pyautogui as pg
import speech_recognition as sr
import pyttsx3
import pywhatkit
import random
import requests
import json
import time
# ============================================================================== Librerias ================
#  >> Carga de archivos
# ---------------------------------------------------------------------------------------------------------
with open('data_talk.json', 'r') as file:
    data = json.load(file)

# =========================================================================================================
#  >> Funcionamiento del COMMAND
# ---------------------------------------------------------------------------------------------------------
def take_command():                                     # Peticion de la orden
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
# ---------------------------------------------------------------------------------------------------------
def run_nana(order):                                    # Realizacion de la orden
    now = dt.now()
    if 'reproduce' in order.lower():
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
    elif "clima" in order.lower() or "tiempo" in order.lower():
        dat = ""
        if "en " in order:
            dat = "London" # por ahora
        else:
            dat = "Caracas"
        weather(data["weathers"]["urls"]["weather"], data["weathers"]["urls"]["location"], dat, data["weathers"]["key"])
    elif "repetir" in order.lower() or "repite" in order.lower():
        repeat(order.replace("repetir", "").replace("repite", ""))
    elif "cuentame" in order.lower() or "quien soy" in order.lower() or "chiste" in order.lower() or "cuento" in order.lower() or "historia" in order.lower() or "aforismo" in order.lower() or "frase" in order.lower():
        tell(order)
    else:           # realizara la consulta automaticamente en el internet
        talk("De " + order + " " + data["result"][random.randint(0, len(data["result"])-1)])
        lista = GoogleSearch().search(order)
        valor = ""
        for i in lista:
            if valor == "":
                valor = i
                break
        webbrowser.open_new_tab(valor)
# =========================================================================================================
#   >> Funciones de la APP
# ---------------------------------------------------------------------------------------------------------
def weather(url_t, url_loc, city, key):         # Consultar clima
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
# ---------------------------------------------------------------------------------------------------------
def send_nana(json,persona, mensaje):           # Enviar un mensaje
    now = dt.now()
    for k,v in json.items():
        if persona == k:
            pywhatkit.sendwhatmsg_instantly(v, mensaje, 30, True, 22)
            pg.press("enter")
# ---------------------------------------------------------------------------------------------------------
def talk(text):
    nanavoice = pyttsx3.init()
    nanavoice.setProperty('rate', 150)
    nanavoice.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
    print(text)
    nanavoice.say(text)
    nanavoice.runAndWait()

# ---------------------------------------------------------------------------------------------------------
def tell(x):
    if "quien soy" in x:
        now = dt.now()
        y,z,w = (int(str(data["perfil"]["cumpleaos"][0:1]))), (int(str(data["perfil"]["cumpleaos"][3:4]))), ((now.year) - int(str(data["perfil"]["cumpleaos"][6:10])))
        if now.day >= y and now.month >= z:
            w += 1
        talk("Tu eres: "+ data["perfil"]["Nombre"]+" "+ data["perfil"]["Apellido"]+ ". Naciste el: "+ data["perfil"]["cumpleaos"]+ ", por lo que tienes: " + f"{w-1} años")
    elif "chiste" in x:
        talk(data["tell_phrase"]["comedy"][random.randint(0, len(data["tell_phrase"]["comedy"]))])
    elif "historia" in x or "cuento" in x:
        talk(data["tell_phrase"]["m_story"][random.randint(0, len(data["tell_phrase"]["m_story"]))])
    elif "aforismo" in x or "frase" in x:
        talk(data["tell_phrase"]["phrase"][random.randint(0, len(data["tell_phrase"]["phrase"]))])
# ---------------------------------------------------------------------------------------------------------
def repeat(frase):
    if frase != "":
        sleep(2)
        talk(frase)
    else:
        talk(data["error"][0][random.randint(0, len(data["error"][0]))], ", ",data["error"][1][random.randint(0, len(data["error"][1]))])
# ---------------------------------------------------------------------------------------------------------
def notify_fech():
    now = dt.now()
    if data["perfil"]["cumpleaos"] == f"{now.day}-{now.month}-{now.year}":
        x,y = ((now.year) - data["perfil"]["cumpleaos"][6:10]), data["perfil"]["Nombre"]
        talk(f"FELICIDADES {y} , HOY ES TU CUMPLEAÑOS NUMERO {x}") #AÑADIR tambien como RECORDATORIO
# ---------------------------------------------------------------------------------------------------------
#def salud(illness):
#    checkbox_click(self, instance, value, enfermedad)
#    talk(checkbox_click)
# ---------------------------------------------------------------------------------------------------------
def show_notification(self, tittle, message):  # usando plyer
    notification.notify(
        title=tittle,
        message=message,
        timeout=10,
        app_name="Nana",
        app_icon="./Images/LOGO NANA.ico"
    )
#def checkbox_click(self, instance, value, enfermedad):
#    enfermedades = []
#    if value == True:
#        PersonScreen.enfermedades.append(enfermedad)
#        output = ''
#        for x in MyLayout.checks:
#            output = f'{output} {x}'
#        self.ids.output_label.text = f"{output}"
#    else:
#        PersonScreen.enfermedades.remove(enfermedad)
#        output = ''
#        for x in MyLayout.checks:
#            output = f'{output} {x}'
#        self.ids.output_label.text = f"{output}"
#    return output

# ---------------------------------------------------------------------------------------------------------
