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
# ============================================================================== Archivos
import function as f


class NanaApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return

    def callback(self):
        print("Preparando escucha...")
        f.talk('Hola, soy Nana. ¿Qué puedo hacer por ti?')
        order = f.take_command()
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
    NanaApp().run()
