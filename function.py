# =========================================================================================================
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
#from googlesearch.googlesearch import GoogleSearch #para solucionar el error de search en mi compu
#import webbrowser
from plyer import notification
from datetime import datetime as dt
from datetime import time
# ============================================================================== Librerias Kivy ===========
import pyautogui as pg
import speech_recognition as sr
#from kvdroid.tools.notification import create_notification
#from kvdroid.tools.contact import get_contact_details
#from kvdroid.jclass.android.graphics import Color
import pyttsx3
import pywhatkit
import random
import requests
import json
import webbrowser
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
    try:
        now = dt.now()
        if order.lower() in 'reproducereproduccionreproducir': # optimizar porfavor
            song = order.replace('reproduce', '')
            talk('Reproduciendo ' + song)
            pywhatkit.playonyt(song)
        elif 'mensaje' in order.lower():
            # se debe implementar una opci??n que deje buscar contactos por nombre, y extraer el n??mero de ah??
            talk('??Qu?? quieres decirle?')
            mensaje = take_command()
            # n??mero de angelica como prueba
            pywhatkit.sendwhatmsg_instantly('+584120999401', mensaje, 11, True, 6)
        elif "hoy" in order or "fecha" in order.lower():
            talk(f"Hoy estamos a {now.day} de {now.month} del a??o {now.year}")
        elif "hora" in order.lower():
            talk(f"Son las {now.hour} horas con {now.minute} minutos")
        elif "recordatorio" in order.lower():
            talk("??Que desea recordar?")
            mensaje = take_command()
        elif "hipertenso" in order.lower(): # Modificar cuando tengamos la BD implementada # ["hipertenso", "hipertensa", "hipertension"]
            #notify()
            salud("hipertenso") # https://www.medicalnewstoday.com/articles/es/alimentos-a-evitar-con-presion-arterial-alta#alimentos-salados
        elif  "diabetes" in order.lower(): #["diabetes", "diabetico", "diabetica", "diabete"]
            salud("diabetes")
        elif "clima" in order.lower() or "tiempo" in order.lower():
            dat = ""
            if "en " in order:
                dat = "Caracas" # por ahora
            else:
                dat = "London"
            weather(data["weathers"]["urls"]["weather"], data["weathers"]["urls"]["location"], dat, data["weathers"]["key"])
        elif "repetir" in order.lower() or "repite" in order.lower():
            repeat(order.replace("repetir", "").replace("repite", ""))
        elif "cuentame" in order.lower() or "quien soy" in order.lower() or "chiste" in order.lower() or "cuento" in order.lower() or "historia" in order.lower() or "aforismo" in order.lower() or "frase" in order.lower():
            tell(order)
        else:           # realizara la consulta automaticamente en el internet
            if order == "":
                talk("No escuche nada")
            else:
                talk("De " + order + " " + data["result"][random.randint(0, len(data["result"])-1)])

                webbrowser.open_new_tab(order)
    except:
        print('error externo')
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
        talk(f"Clima: {clima}, Descripcion: {desc}, Temperatura promedio: {temp}C??, Humedad: {humb}, viento a velocidad de: {v_sp} sopla en direccion de {direc} con nubosidad de {numb} puntos")
    except:
        print("Error de busqueda")
        weather(url_t, url_loc, "Caracas", key)
# ---------------------------------------------------------------------------------------------------------
def send_nana(json,persona, mensaje):           # Enviar un mensaje
    try:
        now = dt.now()
        for k,v in json.items():
            if persona == k:
                pywhatkit.sendwhatmsg_instantly(v, mensaje, 30, True, 22)
                pg.press("enter")
    except:
        print("error secundario")
# ---------------------------------------------------------------------------------------------------------
def talk(text):
    nanavoice = pyttsx3.init()
    nanavoice.setProperty('rate', 150)
    nanavoice.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0")
    print(text)
    nanavoice.say(text)
    nanavoice.runAndWait()
# ---------------------------------------------------------------------------------------------------------
'''def notify():
        Notification().open(
            title="Recordatorio",
            icon="./Images/logo blanco.png",
            message="Los granos integrales son preferibles a los productos de harina blanca o pasta para la hipertensi??n",
            timeout=5,
        )'''
# ---------------------------------------------------------------------------------------------------------
def tell(x):
    try:
        if "quien soy" in x:
            now = dt.now()
            y,z,w = (int(str(data["perfil"]["cumpleaos"][0:1]))), (int(str(data["perfil"]["cumpleaos"][3:4]))), ((now.year) - int(str(data["perfil"]["cumpleaos"][6:10])))
            if now.day >= y and now.month >= z:
                w += 1
            talk("Tu eres: "+ data["perfil"]["Nombre"]+" "+ data["perfil"]["Apellido"]+ ". Naciste el: "+ data["perfil"]["cumpleaos"]+ ", por lo que tienes: " + f"{w-1} a??os")
        elif x in "chistecomediarisa":
            talk(data["tell_phrase"]["comedy"][random.randint(0, len(data["tell_phrase"]["comedy"]))])
        elif "historia" in x or "cuento" in x:
            talk(data["tell_phrase"]["m_story"][random.randint(0, len(data["tell_phrase"]["m_story"]))])
        elif "aforismo" in x or "frase" in x:
            talk(data["tell_phrase"]["phrase"][random.randint(0, len(data["tell_phrase"]["phrase"]))])
    except:
        print('fallo externo')
# ---------------------------------------------------------------------------------------------------------
def repeat(frase):
    try:
        if frase != "":
            time.sleep(2)
            talk(frase)
        else:
            talk(data["error"][0][random.randint(0, len(data["error"][0]))], ", ",data["error"][1][random.randint(0, len(data["error"][1]))])
    except:
        pass
# ---------------------------------------------------------------------------------------------------------
def notify_fech():
    try:
        now = dt.now()
        if data["perfil"]["cumpleaos"] == f"{now.day}-{now.month}-{now.year}":
            x,y = ((now.year) - data["perfil"]["cumpleaos"][6:10]), data["perfil"]["Nombre"]
            talk(f"FELICIDADES {y} , HOY ES TU CUMPLEA??OS NUMERO {x}")# A??ADIR tambien como RECORDATORIO
    except:
        pass
# ---------------------------------------------------------------------------------------------------------
def salud(illness):
    tell = ["", ""]
    for i in data["salud"]["frase"]:
        tell[0] += i[random.randint(0, len(i)-1)] + " "
    tell[0] += "."
    if illness == "diabetes":
        tell[1] = "dbetes"
    else:
        tell[1] = "hipert"
    for i in range(1, len(data["salud"][tell[1]])+1):
        temp = data["salud"][tell[1]][i-1]
        tell[0] += f"{i}, {temp}. "
    talk(tell[0])
# ---------------------------------------------------------------------------------------------------------
def show_notification(self, tittle, message): #usando plyer
    notification.notify(
        title=tittle,
        message=message,
        timeout=10,
        app_name="Nana",
        app_icon="./Images/LOGO NANA.ico"
    )

'''def show_notificacions(self, tittle, message): #usando kvdroid 
    create_notification(
        small_icon="./Images/LOGO NANA.ico",  # app icon
        channel_id="1", title="You have a message",
        text="hi, just wanted to check on you",
        ids=1, channel_name=f"ch1",  # no se de que se trata esto
        large_icon="assets/image.png",  # creo que esto es el icono que va al lado del texto
        expandable=True,
        small_icon_color=Color().rgb(0x00, 0xCC, 0x00),  # 0x00 0xCC 0x00 para lightgreen 00CC00
        big_picture="assets/image.png"  # esto tampoco se que es
    )'''
# ---------------------------------------------------------------------------------------------------------
'''phone_book=get_contact_details("phone_book")  # gets a dictionary of all contact both contact name and phone mumbers
nombres = get_contact_details("names")  # gets a list of all contact names
tlf = get_contact_details("mobile_no")  # gets a list of all contact phone numbers

def extraer_contactos(self, nombres, tlf):
    for y in tlf:
        for i in nombres:
            contactos[y] = i'''

# ---------------------------------------------------------------------------------------------------------
