#r request.py
import requests

def obtener_datos_endpoint():
    url = "http://192.168.2.39:4000/api/site_settings/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos del endpoint: {response.status_code}")
        return []
