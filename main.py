# ============================================================================== INTERFAZ
from turtle import width
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
# ============================================================================== Librerias
from pyautogui import sleep
import speech_recognition as sr
import pyttsx3
import pywhatkit
from time import sleep
import random
# ============================================================================== Archivos
import function as f
import json

with open('data_talk.json', 'r') as file:
    data = json.load(file)

class MDScreen(Screen):
    pass
class PersonScreen(Screen):
#    def on_checkbox_active(self, checkbox, value):
        #if value == True:
 #
        #    print("y")
        #else:
#
        #    print("x")
        pass
class NanaApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return

    def callback(self):
        print("Preparando escucha...")
        word = ""
        for i in data["Quest"]:
            x = random.randint(0, len(i)-1)
            word += i[x] + " "
        f.talk(word)
        order = f.take_command()
        f.talk(data["query"][random.randint(0, len(data["query"])-1)])
        f.run_nana(order)

    def search(self):
        order = self.root.ids.data.text
        f.run_nana(order)
        self.root.ids.data.text = ""

    def send_people(self):
        json = {"wilt":"+584123080460",
                "angelica":"+584120999401"}
        persona = self.root.ids.people.text
        mensaje = self.root.ids.msg.text
        f.send_nana(json,persona,mensaje)
        self.root.ids.people.text = ""
        self.root.ids.msg.text = ""

if __name__ == "__main__":
    f.talk(data["welcome"][random.randint(0, len(data["welcome"])-1)] + " " + data["Quest"][1][random.randint(0, len(data["Quest"][1])-1)] + " " + data["Quest"][2][random.randint(0, len(data["Quest"][2])-1)])
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