# =========================================================================================================
from plyer import notification
from googlesearch.googlesearch import GoogleSearch #para solucionar el error de search en mi compubrew install portaudiobrew install portaudio
import webbrowser
# ============================================================================== Librerias Kivy ===========
import pyautogui as pg
import speech_recognition as sr
from datetime import datetime as dt
import pyttsx3
import pywhatkit
import random
import requests
import json
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
    if order.lower() in 'reproduce-reproducir-reproduccion-produce-toca-canta':
        song = order.replace('reproduce', '')
        talk('Reproduciendo ' + song)
        pywhatkit.playonyt(song)
    elif order.lower() in 'mensaje-enviar-whatsapp-wasa-escribir-escribe':
        # se debe implementar una opción que deje buscar contactos por nombre, y extraer el número de ahí
        talk('¿Qué quieres decirle?')
        mensaje = take_command()
        # número de angelica como prueba
        pywhatkit.sendwhatmsg_instantly('+584120999401', mensaje, 11, True, 6)
    elif order.lower() in "hoy-fecha-cuando estamos-que dia es":
        talk(f"Hoy estamos a {now.day} de {now.month} del año {now.year}")
    elif order.lower() in "hora":
        talk(f"Son las {now.hour} horas con {now.minute} minutos")
    elif order.lower() in "recordatorio-recuerdame":
        talk("¿Que desea recordar?")
        mensaje = take_command()
    elif order.lower() in "clima-tiempo-temperatura-ambiente":
        dat = ""
        if "en " in order:
            dat = "Caracas" # por ahora
        else:
            dat = "London"
        weather(data["weathers"]["urls"]["weather"], data["weathers"]["urls"]["location"], dat, data["weathers"]["key"])
    elif order.lower() in "repetir-repite":
        repeat(order.replace("repetir", "").replace("repite", ""))
    elif order.lower() in "quien soy-chiste-cuentame un chiste-cuento-historia-aforismo-frase":
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
def show_notification(self, tittle, message):  # usando plyer
    notification.notify(
        title=tittle,
        message=message,
        timeout=10,
        app_name="Nana",
        app_icon="./Images/LOGO NANA.ico"
    )
# ---------------------------------------------------------------------------------------------------------
