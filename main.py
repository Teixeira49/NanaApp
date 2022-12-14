from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.pickers import MDTimePicker
from kivymd.uix.list import MDList, ThreeLineListItem
from datetime import date, datetime
#Base de datos
'''import firebase_admin
from firebase_admin import credentials
from firebase_admin import db'''

# ============================================================================== Librerias Kivy ===========
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
class ContactoScreen(Screen):
    pass
class ListaConScreen(Screen):
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

    def notificar_recordatorio(self, eventos):
        today = date.today()
        now = datetime.now()
        if today == eventos[today].key() and now == eventos[now].key():
            f.show_notification("Recordatorio", eventos.eventos[today][now])
        else:
            pass

    def save_contact(self):
        nombre = self.root.get_screen('ContactoScreen').ids.contact_name.text
        apellido = self.root.get_screen('ContactoScreen').ids.contact_lastname.text
        tlf = self.root.get_screen('ContactoScreen').ids.phone_number.text
        self.contactos={}
        if apellido not in self.contactos.keys():
            self.contactos[nombre] = {}
            self.contactos[nombre][apellido] = str(tlf)
        else:
            self.contactos[nombre][apellido] = str(tlf)

        print(self.contactos)

        self.root.get_screen('ContactoScreen').ids.name_label.text = ""
        self.root.get_screen('ContactoScreen').ids.lastname_label.text = ""
        self.root.get_screen('ContactoScreen').ids.tlf_label.text = ""

    def appnt_listCon(self):
        for i in list(self.contactos.keys()):
            for y in list(self.contactos[i].keys()):
                items = ThreeLineListItem(text=str(i+" "+y), secondary_text=str(self.contactos[i][y]), tertiary_text="cpnyactos")
        self.root.get_screen('ListaConScreen').ids.ContactContainer.add_widget(items)
# ---------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    NanaApp().run()
    #NanaApp().show_notification("hey user", "take a break now")
    #NanaApp().notificar_recordatorio(eventos)
