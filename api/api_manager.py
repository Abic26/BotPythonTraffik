import requests
import os
import json
from dotenv import load_dotenv

class APIManager:
    def __init__(self):
        load_dotenv()
        self.endpoint_url = os.getenv("replace_environment_variable") #reemplaza con tu variable de entorno
        
#EXAMPLE
    # def get_campaign_urls(self):
    #     response = requests.get(self.endpoint_url)
    #     response.raise_for_status()
    #     datos = response.json()
    #     return [(item['url'], item['id_campaigns']) for item in datos]

    # def post_mobile_metrics(self, id, mobile_data):
    #     headers = {'Content-Type': 'application/json'}
    #     response = requests.post(self.endpoint_movil, headers=headers, data=json.dumps(mobile_data))
    #     return response

    # def post_desktop_metrics(self, id, desktop_data):
    #     headers = {'Content-Type': 'application/json'}
    #     response = requests.post(self.endpoint_desktop, headers=headers, data=json.dumps(desktop_data))
    #     return response

    # def create_mobile_data(self, id, scores, current_date):
    #     return {
    #         "id_campaigns": id,
    #         "mobile_date": current_date,
    #         "mobile_performance": int(scores.get('Rendimiento', 0)),
    #         "mobile_accessibility": int(scores.get('Accesibilidad', 0)),
    #         "mobile_practices": int(scores.get('Prácticas recomendadas', 0)),
    #         "mobile_seo": int(scores.get('SEO', 0))
    #     }

    # def create_desktop_data(self, id, scores, current_date):
    #     return {
    #         "id_campaigns": id,
    #         "desktop_date": current_date,
    #         "desktop_performance": int(scores.get('Rendimiento', 0)),
    #         "desktop_accessibility": int(scores.get('Accesibilidad', 0)),
    #         "desktop_practices": int(scores.get('Prácticas recomendadas', 0)),
    #         "desktop_seo": int(scores.get('SEO', 0))
    #     }
        