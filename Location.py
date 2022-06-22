from takecmd import Speak
import requests

def location():
    Speak("wait sir,let me check")
    try:
        
        ip=requests.get('https://api.ipify.org').text
        url='https://get.geojs.io/v1/ip/geo/'+ip+'.json'
        geo_request=requests.get(url)
        geo_data=geo_request.json()
        print(geo_data)
        city=geo_data['city']
        # state=geo_data['state']
        country=geo_data['country']
        Speak(f"Sir i am not sure,but i think we are in {city} city of  {country}country")

    except Exception as e:
        Speak("Sorry sir, due to network issue i am not able to find where we are")
        pass

