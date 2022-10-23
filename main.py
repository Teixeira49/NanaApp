from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
import speech_recognition as sr
import pyttsx3
import pywhatkit



class MyLayout(Widget):
    def callback(self):

        listener = sr.Recognizer()
        voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0"
        nanavoice = pyttsx3.init()
        nanavoice.setProperty("voice", voice_id)
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
            except:
                pass
            return command

        def run_nana():
            command = take_command()
            if 'reproduce' in command:
                song = command.replace('reproduce', '')
                talk('Reproduciendo ' + song)
                pywhatkit.playonyt(song)

            if 'mensaje' in command:
                #se debe implementar una opción que deje buscar contactos por nombre, y extraer el número de ahí
                talk('¿Qué quieres decirle?')
                mensaje = take_command()
                #número de angélica como prueba
                #debería mandar el mensaje automáticamente
                pywhatkit.sendwhatmsg_instantly('+584120999401', mensaje, 3, True, 3)


        run_nana()

class NanaApp(App):
    def build(self):
        return MyLayout()





if __name__ == "__main__":
    NanaApp().run()
