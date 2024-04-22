from datetime import datetime 
import requests
import json


def ri3valeur(L):
  L1=[]
  for i in range(0,len(L),3):
      L1.append(L[i])
  return L1

dateLyouma=datetime.today().strftime("%Y-%m-%d")
dateLyouma2=datetime.today().strftime("%d-%m-%Y")
lyoumaName=datetime.today().strftime("%A")
jours={'Monday':'Lundi','Tuesday':'Mardi', 'Wednesday':'Mercredi', 'Thursday':'jeudi', 'Friday':'Vendredi', 'Saturday':'samedi','Sunday':'Dimanche'}
Lyouma=jours[lyoumaName]
url="https://api.open-meteo.com/v1/forecast?"
url=url+"latitude=31,51&longitude=-9,77"
# url=url+"latitude="+atit+",51&longitude="+long
url=url+"&hourly=temperature_2m"
url=url+"&hourly=windspeed_10m"
url=url+"&hourly=cloud_cover"
url=url+"&hourly=precipitation"
url=url+"&daily=sunrise"
url=url+"&daily=sunset"
url=url+"&start_date="+dateLyouma
url=url+"&end_date="+dateLyouma



response=requests.get(url)
response=requests.get(url).content.decode('utf-8')
Data = json.loads(response)


daytemperature=Data[0]['hourly']['temperature_2m']
windsliste=Data[0]['hourly']['windspeed_10m']
cloudcover=Data[0]['hourly']['cloud_cover']
precipitation=Data[0]['hourly']['precipitation']
sunrise=Data[0]['daily']['sunrise']
sunset=Data[0]['daily']['sunset']

listetemperature=ri3valeur(daytemperature)
listewind=ri3valeur(windsliste)
listcloud=ri3valeur(cloudcover)
listprecipitation=ri3valeur(precipitation)


def Data1():
    dataMeteo=[ { "temps":"","temperature":"","wind":"","precipitation":"","image":"" } for i in range(8) ]
    for i in range(8):
        dataMeteo[i]["temps"]=str(i*3)+":00"
        dataMeteo[i]["temperature"]=listetemperature[i]
        dataMeteo[i]["precipitation"]=listprecipitation[i]
        dataMeteo[i]["wind"]=listewind[i]
    return dataMeteo    
dataMeteo2= Data1()

sunr=sunrise[0][11:13]
suns=sunset[0][11:13]

for i in range(8):
    # Heure du jour (entre lever et coucher du soleil)
    if i * 3 >= int(sunr) and i * 3 < int(suns):
        # Couverture nuageuse
        if cloudcover[i] < 50:
            # Peu de nuages pendant la journée
            dataMeteo2[i]["image"] = "static/images/sunmorecloud.png"
        else:
            # Beaucoup de nuages pendant la journée
            dataMeteo2[i]["image"] = "static/images/cloud.png"
        # Précipitation
        if dataMeteo2[i]["precipitation"] > 5:
            # Pluie pendant la journée
            dataMeteo2[i]["image"] = "static/images/rain.png"
    else:
        # Heure de la nuit
        # Couverture nuageuse
        if cloudcover[i] < 50:
            # Peu de nuages pendant la nuit
            dataMeteo2[i]["image"] = "static/images/mooncloud.png"
        else:
            # Beaucoup de nuages pendant la nuit
            dataMeteo2[i]["image"] = "static/images/moon.png"
        # Précipitation
        if dataMeteo2[i]["precipitation"] > 5:
            # Pluie pendant la nuit
            dataMeteo2[i]["image"] = "static/images/rain.png"

