from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import speech_recognition as sr
import pyttsx3
import pywhatkit

class NanaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Green"
        return
    def callback(self):

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

        def take_command():

            try:
                with sr.Microphone() as source:
                    print("Escuchando...")
                    listener.adjust_for_ambient_noise(source)
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    print(command)
                    return command
            except:
                pass


        def run_nana():
            order = take_command()
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

        run_nana()


if __name__ == "__main__":
    NanaApp().run()
