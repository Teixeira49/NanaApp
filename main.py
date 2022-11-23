# =========================================================================================================
from turtle import width
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
# ============================================================================== Librerias Kivy ===========
import function as f
import json
import random
import webbrowser
from tkinter import *
#from tkcalendar import Calendar 
# ============================================================================== Archivos =================
#  >> Carga de archivos:
# ---------------------------------------------------------------------------------------------------------
with open('data_talk.json', 'r') as file:
    data = json.load(file)
# ---------------------------------------------------------------------------------------------------------
#  >> Paneles
# ---------------------------------------------------------------------------------------------------------
class MDScreen(Screen):
    pass
class PersonScreen(Screen):
    pass
class CalendarScreen(Screen):
    pass
class SmsScreen(Screen):
    pass
class NanaApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Green"
        return

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

    def profile(self):
        webbrowser.open_new_tab(
            'https://www.google.com/search?q=como+crear+perfil&client=opera-gx&sxsrf=ALiCzsbEvkZRB-XStGjrA7B8OmgWvB8rdg%3A1667780750279&ei=jlBoY97aEJyZwbkPuKOL-Ac&ved=0ahUKEwje2bu555r7AhWcTDABHbjRAn8Q4dUDCA4&uact=5&oq=como+crear+perfil&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEEcQ1gQQsAM6BwgAELADEEM6DQgAEOQCENYEELADGAE6BAgjECc6CggAEIAEEIcCEBQ6CAgAELEDEIMBOgUIABCxAzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOggIABCABBDJA0oECE0YAUoECEEYAEoECEYYAVCCzgNYnuwDYLPuA2gCcAF4AoABvgWIAY0gkgENMi44LjIuMy4wLjEuMZgBAKABAcgBEcABAdoBBggBEAEYCQ&sclient=gws-wiz-serp')

    def call(self):
        webbrowser.open_new_tab(
            'https://www.google.com/search?q=como+llamar&client=opera-gx&sxsrf=ALiCzsbpqNiZ73J-mRKVXwcrIKb2JxxmEw%3A1667780733762&ei=fVBoY7qXLsyGwbkPn-CfyAI&ved=0ahUKEwj6ycux55r7AhVMQzABHR_wBykQ4dUDCA4&uact=5&oq=como+llamar&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQgAQQhwIQFDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCCMQ6gIQJzoECCMQJzoKCC4QxwEQ0QMQQzoICAAQgAQQsQM6CwgAEIAEELEDEIMBOg4ILhCABBCxAxDHARDRAzoRCC4QgAQQsQMQgwEQxwEQ0QM6DQguEMcBENEDENQCEEM6BwgAEIAEEAM6CAgAELEDEIMBOgQIABBDOgsIABCABBCxAxDJAzoLCC4QgAQQsQMQgwE6CAguEIAEENQCSgQITRgBSgQIQRgASgQIRhgAUABY3g5g5RJoAXABeACAAe8BiAGmDZIBBTAuOC4zmAEAoAEBsAEKwAEB&sclient=gws-wiz-serp')

    
    def agendar(self):
        root = Tk() 
        root.geometry("400x400")  
        cal = Calendar(root, selectmode = 'day', year = 2022, month = 11, day = 24)   
        cal.pack(pady = 20) 
        
        def grad_date(): 
            date.config(text = "Selected Date is: " + cal.get_date()) 
            var = cal.get_date()
            with open("fecha.txt", "a") as file:
                file.write(var)
            root.destroy()
            
        
        Button(root, text = "Elegir fecha", command = grad_date).pack(pady = 20) 
        
        date = Label(root, text = "") 
        date.pack(pady = 20)

        
        root.mainloop()


        with open("fecha.txt", "a") as file:
                file.write(f" {self.root.get_screen('CalendarScreen').ids.recordatorio.text}")
                file.write("\n")
        self.root.get_screen('CalendarScreen').ids.recordatorio.text = ""




    def search(self):
        order = self.root.get_screen('MDScreen').ids.data.text
        self.root.get_screen('MDScreen').ids.data.text = ''
        f.run_nana(order)

    def send_people(self):
        with open('contactos.txt', 'r') as g:
            lineas = g.readlines()
            llamar = [l.split() for l in lineas]

            for i in llamar:
                if i == []:
                    llamar.remove([])
            for i in llamar:
                if len(i[0].split(sep=':')) < 2:
                    llamar.remove(i)
            for i in llamar:
                if len(i) > 1:
                    new = ""
                    new += (i[0].split(sep=':'))[1]
                    cont = 1
                    for j in i:
                        new += " "
                        new += str(i[cont])
                        cont += 1
                        if j == i[-2]:
                            break

                    new2 = ''
                    new2 += (i[0].split(sep=':'))[0]
                    new2 += ':'
                    new2 += new

                    i[0] = new2
                    while len(i) > 1:
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

            diccionario = {}
            cont = 0
            while cont < len(lista_nombre2):
                diccionario[lista_nombre2[cont]] = lista_tlf2[cont]
                cont += 1


        persona = self.root.get_screen('SmsScreen').ids.people.text
        mensaje = self.root.get_screen('SmsScreen').ids.msg.text
        f.send_nana(diccionario, persona, mensaje)
        self.root.get_screen('SmsScreen').ids.people.text = ""
        self.root.get_screen('SmsScreen').ids.msg.text = ""
# ---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    NanaApp().run()
# ---------------------------------------------------------------------------------------------------------