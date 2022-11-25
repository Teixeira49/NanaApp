#En el terminal poner
# Android min-api21
# pip install kvdroid
# requirement = kvdroid

from kvdroid.tools.contact import get_contact_details
from kvdroid.jclass.android.graphics import Color
from kvdroid.tools.notification import create_notification
from kvdroid.tools import get_resource

create_notification(
    small_icon=get_resource("drawable").ico_nocenstore,  # app icon
    channel_id="1", title="You have a message",
    text="hi, just wanted to check on you",
    ids=1, channel_name=f"ch1",  #no se de que se trata esto
    large_icon="assets/image.png",  #creo que esto es el icono que va al lado del texto
    expandable=True, 
    small_icon_color=Color().rgb(0x00, 0xCC, 0x00),  # 0x00 0xCC 0x00 para lightgreen 00CC00
    big_picture="assets/image.png" #esto tampoco se que es
)

get_contact_details("phone_book") # gets a dictionary of all contact both contact name and phone mumbers
get_contact_details("names") # gets a list of all contact names
get_contact_details("mobile_no") # gets a list of all contact phone numbers
