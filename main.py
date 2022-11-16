# ============================================================================== INTERFAZ
from turtle import width
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
<<<<<<< HEAD
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

# ============================================================================== Librerias
from pyautogui import sleep
=======
from kivy.garden.notification import Notification
>>>>>>> 9cef50ccbb8d41173dc0e8ab403d805ca8c1bf40
import speech_recognition as sr
import pyttsx3
import pywhatkit
from time import sleep
import random
# ============================================================================== Archivos
import function as f
import time
import serial
import webbrowser
import json

with open('data_talk.json', 'r') as file:
    data = json.load(file)

class MDScreen(Screen):
    pass
class PersonScreen(Screen):
        #    def on_checkbox_active(self, checkbox, value):
        # if value == True:
        #
        #    print("y")
        # else:
        #
        #    print("x")
    pass
class NanaApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return

<<<<<<< HEAD
=======

>>>>>>> 9cef50ccbb8d41173dc0e8ab403d805ca8c1bf40
    def callback(self):
        print("Preparando escucha...")
        word = ""
        for i in data["Quest"]:
            x = random.randint(0, len(i) - 1)
            word += i[x] + " "
        f.talk(word)
        order = f.take_command()
        f.talk(data["query"][random.randint(0, len(data["query"]) - 1)])
        f.run_nana(order)

    def search(self):
        order = self.root.get_screen('MDScreen').ids.data.text
        self.root.get_screen('MDScreen').ids.data.text = ''

        f.run_nana(order)



    def profile(self):
        webbrowser.open_new_tab('https://www.google.com/search?q=como+crear+perfil&client=opera-gx&sxsrf=ALiCzsbEvkZRB-XStGjrA7B8OmgWvB8rdg%3A1667780750279&ei=jlBoY97aEJyZwbkPuKOL-Ac&ved=0ahUKEwje2bu555r7AhWcTDABHbjRAn8Q4dUDCA4&uact=5&oq=como+crear+perfil&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQ1gQQsAM6BwgAELADEEM6DQgAEOQCENYEELADGAE6BAgjECc6CggAEIAEEIcCEBQ6CAgAELEDEIMBOgUIABCxAzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOggIABCABBDJA0oECE0YAUoECEEYAEoECEYYAVCCzgNYnuwDYLPuA2gCcAF4AoABvgWIAY0gkgENMi44LjIuMy4wLjEuMZgBAKABAcgBEcABAdoBBggBEAEYCQ&sclient=gws-wiz-serp')
    def call(self):
        webbrowser.open_new_tab('https://www.google.com/search?q=como+llamar&client=opera-gx&sxsrf=ALiCzsbpqNiZ73J-mRKVXwcrIKb2JxxmEw%3A1667780733762&ei=fVBoY7qXLsyGwbkPn-CfyAI&ved=0ahUKEwj6ycux55r7AhVMQzABHR_wBykQ4dUDCA4&uact=5&oq=como+llamar&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoKCC4QxwEQ0QMQQzoICAAQgAQQsQM6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoRCC4QgAQQsQMQgwEQxwEQ0QM6DQguEMcBENEDENQCEEM6BwgAEIAEEAM6CAgAELEDEIMBOgQIABBDOgsIABCABBCxAxDJAzoLCC4QgAQQsQMQgwE6CAguEIAEENQCSgQITRgBSgQIQRgASgQIRhgAUABY3g5g5RJoAXABeACAAe8BiAGmDZIBBTAuOC4zmAEAoAEBsAEKwAEB&sclient=gws-wiz-serp')

    def send_people(self):


        with open('contactos.txt', 'r') as g:
            lineas = g.readlines()
            llamar = [l.split() for l in lineas]

            for i in llamar:
                if i == []:
                    llamar.remove([])
            for i in llamar:
                if len(i[0].split(sep=':')) <2:
                    llamar.remove(i)
            for i in llamar:
                if len(i)>1:
                    new = ""
                    new += (i[0].split(sep=':'))[1]
                    cont = 1
                    for j in i:
                        new += " "
                        new += str(i[cont])
                        cont+=1
                        if j == i[-2]:
                            break

                    new2 = ''
                    new2 += (i[0].split(sep=':'))[0]
                    new2 += ':'
                    new2 += new

                    i[0] = new2
                    while len(i)>1:
                        i.pop(-1)

            llamar2 = []
            for i in llamar:
                if not i in llamar2:
                    llamar2.append(i)

            print(llamar2)

            lista_nombre = []
            lista_tlf = []
            while len(llamar2) > 0:
                if list(llamar2[0][0])[0] == 'N' and list(llamar2[1][0])[0] == 'P':
                    lista_nombre.append((llamar2[0][0]))
                    lista_tlf.append((llamar2[1][0]))
                    llamar2.remove(llamar2[0])
                    llamar2.remove(llamar2[1])
                else:
                    llamar2.remove(llamar2[0])


            lista_nombre2 = []
            for i in lista_nombre:
                x = i.replace('Name:', "")
                lista_nombre2.append(x)

            lista_tlf2 = []
            for i in lista_tlf:
                x = i.replace('PhoneNumber:', "")
                lista_tlf2.append(x)

<<<<<<< HEAD
            diccionario = {}
            cont = 0
            while cont < len(lista_nombre2):
                diccionario[lista_nombre2[cont]] = lista_tlf2[cont]
                cont += 1
=======
        listener = sr.Recognizer()
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
        nanavoice = pyttsx3.init()
        nanavoice.setProperty("voice", voice_id)
        nanavoice.setProperty('rate', 150)
        nanavoice.say('Hola, soy Nana. ¿Qué puedo hacer por ti?')
        nanavoice.runAndWait()

        def talk(text):
            nanavoice.say(text)
            nanavoice.runAndWait()

        def notify():
            Notification().open(
                title="Recordatorio",
                icon="./Images/logo blanco.png",
                message="Los granos integrales son preferibles a los productos de harina blanca o pasta para la hipertensión",
                timeout=5,
            )
        def take_command():
            command = ''
            try:
                with sr.Microphone() as source:
                    print("Escuchando...")
                    listener.adjust_for_ambient_noise(source)
                    voice = listener.listen(source)
                    listener.recognize_google(voice, language="es-VE")
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    print(command)
            except:
                pass
            return command

        def run_nana():
            order = take_command()
            notify()
            if 'reproduce' in order:
                song = order.replace('reproduce', '')
                talk('Reproduciendo ' + song)
                pywhatkit.playonyt(song)

            if 'mensaje' in order:
                # se debe implementar una opción que deje buscar contactos por nombre, y extraer el número de ahí
                talk('¿Qué quieres decirle?')
                mensaje = take_command()
                # número de angelica como prueba
                pywhatkit.sendwhatmsg_instantly('+584120999401', mensaje, 11, True, 6)

            if 'busca' in order:
                busqueda = order.replace('busca', '')
                pywhatkit.search(busqueda)

        run_nana()
>>>>>>> 9cef50ccbb8d41173dc0e8ab403d805ca8c1bf40

            print(diccionario)





        json = {"wilt":"+584123080460",
                "angelica":"+584120999401"}



        persona = self.root.get_screen('MDScreen').ids.people.text
        mensaje = self.root.get_screen('MDScreen').ids.msg.text
        f.send_nana(diccionario,persona,mensaje)
        self.root.get_screen('MDScreen').ids.people.text = ""
        self.root.get_screen('MDScreen').ids.msg.text = ""

if __name__ == "__main__":
    f.talk(data["welcome"][random.randint(0, len(data["welcome"]) - 1)] + " " + data["Quest"][1][random.randint(0, len(data["Quest"][1]) - 1)] + " " + data["Quest"][2][random.randint(0, len(data["Quest"][2]) - 1)])

    NanaApp().run()








# DESECHADO DE LA API DEL CLIMA:

# https://home.openweathermap.org/api_keys
# https://www.youtube.com/watch?v=nksauZe87Nw

#url = "https://open-weather13.p.rapidapi.com/city/landon"
#https://openweathermap.org/api/geocoding-api
#https://openweathermap.org/current
#https://home.openweathermap.org/subscriptions/billing_info/onecall_30/base?key=base&service=onecall_30

#headers = {
#	"X-RapidAPI-Key": "6041c295d0msh6fde4576d1068d6p175d6ejsnab02cc5a2ef5",
#	"X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
#}

    #response = requests.request("GET", url, headers=headers)
    #print(response.text)