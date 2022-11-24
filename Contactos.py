#En el terminal poner
# Android min-api21
# pip install kvdroid
# requirement = kvdroid

from kvdroid.tools.contact import get_contact_details

get_contact_details("phone_book") # gets a dictionary of all contact both contact name and phone mumbers
get_contact_details("names") # gets a list of all contact names
get_contact_details("mobile_no") # gets a list of all contact phone numbers
