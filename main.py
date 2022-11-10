from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.pickers import MDDatePicker


class main(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file('nana.kv')

    def on_save(self, instance, value, date_range):
        #self.root.ids.date_label.text = str(value)
        self.root.ids.date_label.text = f'{str(date_range[0])} / {str(date_range[-1])}'
        eventos = {"2000-12-27":"cumple nieto cristian"}
        evento = self.root.ids.date_name.text
        self.root.ids.date_name.text = ""
        eventos[value] = evento

    def on_cancel(self, instance, value):
        self.root.ids.date_label.text = "you clicked cancel"

    #def use(self, instance, value, date_range, on_save, on_cancel):
    #    if on_save == True:
    #        self.root.ids.date_label.text = f'{str(date_range[0])} / {str(date_range[-1])}'
    #        eventos = {"2000-12-27": "cumple nieto cristian"}
    #        evento = self.root.ids.date_name.text
    #        self.root.ids.date_name.text = ""
    #        eventos[value] = evento
    #    elif on_cancel == True:
    #        self.root.ids.date_label.text = "you clicked cancel"
    #    else:
    #        self.root.ids.date_label.text = "error"

    def show_date_picker(self):
        #date_dialog = MDDatePicker(year=2000, month=2, day=14)
        date_dialog = MDDatePicker(mode="range")
        #date_dialog.bind(use=self.use, on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()


main().run()