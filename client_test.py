"""
Terminal üzerinden FastAPI ile sürekli sohbet
"""
# Http istekleri yapmak için
import requests

API_URL = "http://127.0.0.1:8000/chat"

name = input("Adınız: ")
age = int(input("Yaşınız: "))

print("\n Sohbet başladı. Çıkmak için 'quit' yazın")

while True:
    user_msg = input(f"{name}: ")
    if user_msg.lower() == "quit":
        print(" Konuşma sonlandırıldı.")
        break

    payload = {
        "name" : name,
        "age" : age,
        "message" : user_msg
    }

    try: 
        res = requests.post(API_URL, json = payload, timeout = 20)

        if res.status_code == 200:
            print(f"Doktor Asistanı: {res.json()['response']}")
        else:
            print("hata", res.status_code, res.text)
    
    except requests.exceptions.RequestException as e:
        print("Bağlantı Hatası: ", e)

























