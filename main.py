# =========================================================================================================
from turtle import width
from kivy.app import App
from kivy.uix.widget import Widget
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.list import MDList
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, ThreeLineListItem
# ============================================================================== Librerias Kivy ===========
from datetime import datetime as dt
import function as f
import json
import random
import webbrowser
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

class AppointmentScreen(Screen):
    pass
class NanaApp(MDApp):
    eventos = {}
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

    def on_save(self, instance, value, date_range):
        self.root.get_screen('CalendarScreen').ids.date_label.text = f'{str(date_range[0])} / {str(date_range[-1])}'

    def on_cancel(self, instance, value):
        self.root.get_screen('CalendarScreen').ids.date_label.text = ""

    def show_date_picker(self):
        date_dialog = MDDatePicker(mode="range")
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    # Get Time
    def get_time(self, instance, time):
        self.root.get_screen('CalendarScreen').ids.time_label.text = str(time)

    # Cancel
    def on_cancel(self, instance, time):
        self.root.get_screen('CalendarScreen').ids.time_label.text = ""

    def show_time_picker(self):
        from datetime import datetime

        # Define default time
        default_time = datetime.strptime("4:20:00", '%H:%M:%S').time()

        time_dialog = MDTimePicker()
        # Set default Time
        time_dialog.set_time(default_time)
        time_dialog.bind(on_cancel=self.on_cancel, time=self.get_time)
        time_dialog.open()


    def save_event(self):
        time = self.root.get_screen('CalendarScreen').ids.time_label.text
        date = self.root.get_screen('CalendarScreen').ids.date_label.text
        value = self.root.get_screen('CalendarScreen').ids.date_name.text
        if date not in self.eventos.keys():
            self.eventos[date] = {}
            self.eventos[date][time] = value
        else:
            self.eventos[date][time] = value
        print(self.eventos)

        self.root.get_screen('CalendarScreen').ids.time_label.text = ""
        self.root.get_screen('CalendarScreen').ids.date_label.text = ""
        self.root.get_screen('CalendarScreen').ids.date_name.text = ""

    def appnt_list(self):
        for i in list(self.eventos.keys()):
            for y in list(self.eventos[i].keys()):
                items = ThreeLineListItem(text=self.eventos[i][y],
                                          secondary_text=i,
                                          tertiary_text=y)
        self.root.get_screen('AppointmentScreen').ids.container.add_widget(items)

    def saveProfile(self):
        try:
            x,y,z = (self.root.get_screen('PersonScreen').ids.people_da.text), (self.root.get_screen('PersonScreen').ids.people_mo.text), (self.root.get_screen('PersonScreen').ids.people_ye.text)
            if (self.root.get_screen('PersonScreen').ids.people_d.text).isnumeric():
                data["perfil"]["dni"] = self.root.get_screen('PersonScreen').ids.people_d.text
            if self.root.get_screen('PersonScreen').ids.people_n.text != "" and self.root.get_screen('PersonScreen').ids.people_p.text != "":
                data["perfil"]["Nombre"] = self.root.get_screen('PersonScreen').ids.people_n.text
                data["perfil"]["Apellido"] = self.root.get_screen('PersonScreen').ids.people_p.text,
            if dt.strptime(f"{x}-{y}-{z}", '%d-%m-%Y') == True and dt.strptime(f"{x}-{y}-{z}", '%d-%m-%Y') < dt.now():
                data["perfil"]["cumpleaos"] = f"{x}-{y}-{z}"
            c = json.dumps(data, indent="  ")
            with open("data_talk.json", 'w', encoding='utf-8') as f:
                f.write(c)
                f.close()
        except:
            print("Error de generacion")
# ---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    NanaApp().run()
    #NanaApp().show_notification("hey user", "take a break now")
# ---------------------------------------------------------------------------------------------------------