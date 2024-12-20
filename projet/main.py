import requests
import fire
import json

def list_vehicule(address="localhost:8080"):
    try:
        response = requests.get("http://"+address+"/vehicles")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la requête : {e}"

def create_vehicle(address="localhost:8080", shortcode="abcd", battery=12, longitude=20.0, latitude=30.0):
    url = f"http://"+address+"/vehicles"
    headers = {"Content-Type": "application/json"}
    data = {
        "shortcode": shortcode,
        "battery": battery,
        "latitude": latitude,
        "longitude": longitude
    }
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status() 
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de la requête : {e}"



if __name__ == '__main__':
    fire.Fire()
