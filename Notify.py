from plyer import notification
import time

def notifyMe(title, message):
   notification.notify(
       title=title,
       message=message,
       app_icon=None,
       timeout=10,
   )
if __name__ == '__main__':
   while True:
       notifyMe("Hola maria, Es hora del almuerzo", "tu comida esta en la nevera")
       time.sleep(15)

#import os
#
#def notify(title, text):
#    os.system("""
#              osascript -e 'display notification "{}" with title "{}"'
#              """.format(text, title))
#
#notify("Title", "Heres an alert")