import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from takecmd import*


def PhoneInfo(query):
    phone_number=phonenumbers.parse(query)
    print(geocoder.description_for_number(phone_number,'en'))
    Speak(geocoder.description_for_number(phone_number,'en'))
    print(carrier.name_for_number(phone_number,'en'))
    Speak(carrier.name_for_number(phone_number,'en'))








