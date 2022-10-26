from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import speech_recognition as sr
import pyttsx3
import pywhatkit
from kivy.lang import Builder
from kivymd.uix.picker import MDDatePicker

class NanaApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Gray"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('date.kv')


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
            command = ''
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

    def on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        #este es para escoger solo una fecha
        self.root.ids.date_label.text = str(value)
        #este para escoger varias fechas
        self.root.ids.date_label.text = f'{str(date_range[0])} - {str(date_range[-1])}'

    def on_cancel(self, instance, value):
        self.root.ids.date_label_text = "you clicked cancel"

    def show_date_picker(self):
        date_dialog = MDDatePicker(year=2000, month=2, day=14)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def show_date_range_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        run_nana()


if __name__ == "__main__":
    NanaApp().run()
