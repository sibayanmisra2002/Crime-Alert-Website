import phonenumbers
import opencage
import folium
import webbrowser

from phone import number

from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode

key = 'f0f616819ee946668d1e591e5fc9d5a9'

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start = 9)
folium.Marker([lat, lng], popup= location).add_to(myMap)

myMap.save("Location.html")

webbrowser.open_new("http://127.0.0.1:5501/Location.html")