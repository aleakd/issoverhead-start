import time
import requests
from datetime import datetime
import smtplib

my_email = "alepython2419@gmail.com"
password = "ryxeerupdsmwvptr"

MY_LAT = -31.422935
MY_LONG = --64.459637

def satelite_cabeza():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

#Your position is within +5 or -5 degrees of the ISS position.
def es_noche():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now <= sunrise or time_now >= sunset:
        return True

while True:
    time.sleep(60)
    if satelite_cabeza() and es_noche():
            coneccion = smtplib.SMTP("smtp.gmail.com")
            coneccion.starttls()
            coneccion.login(user=my_email, password=password)
            coneccion.sendmail(from_addr=my_email,
                               to_addrs=my_email,
                               msg="Subjet:Satelite\n\n Ahora esta pasando por arriba tuyo el satelite es hora de mirar hacia arriba")





