import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button


class NANA(App):
    def build(self):
        #return Label(text = "No jodaaa")
        boton = Button(text = "Presioname", font_size=30, size_hint=(0.3, 0.1), pos=(250,250), background_color=("blue"))
        return boton







if __name__ == "__main__":
    NANA().run()
