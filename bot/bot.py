# bot.py
from controller.request import obtener_datos_endpoint 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlparse
import time
import random

datos_endpoint = obtener_datos_endpoint()

class Bot:
    def __init__(self, proxy=None):
        self.driver = None
        self.base_url = "https://www.google.com"
        self.proxy = proxy
    
    def initialize_driver(self):
        options = Options()
        options.add_argument('--incognito')
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
        if self.proxy:
            options.add_argument(f'--proxy-server={self.proxy}')
        self.driver = webdriver.Chrome(options=options)

    def open_page(self):
        if self.driver is None:
            self.initialize_driver()
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        time.sleep(random.uniform(2, 4))

    def type_slowly(self, element, text, delay=0.1):
        for char in text:
            element.send_keys(char)
            time.sleep(random.uniform(delay, delay+0.2))

    def search(self, query):
        time.sleep(10)
        search_box = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        self.type_slowly(search_box, query)
        time.sleep(random.uniform(2, 3))
        search_box.send_keys(Keys.ENTER)
        time.sleep(random.uniform(4, 6))
        time.sleep(10)
        self.click_link_or_scroll()

    def click_link_or_scroll(self):
    # Define una lista de URLs objetivo obtenidas del endpoint
        all_link = [item['urls'][0] for item in datos_endpoint if 'urls' in item and item['urls']]  # Limita a 5
        random.shuffle(all_link)
        target_urls = all_link[:10]
        
        # Intenta encontrar y hacer clic en los enlaces
        found_link = False
        for target_url in target_urls:
            url_parseado = urlparse(target_url)
            # Usa tanto el esquema como el netloc para construir el url_base completo
            url_base = f"{url_parseado.scheme}://{url_parseado.netloc}"
            # print(url_base)
            
            # Construye el XPath buscando enlaces que comiencen con el url_base
            xpath = f"//a[starts-with(@href, '{url_base}')]"
            # print(xpath)
            
            links = self.driver.find_elements(By.XPATH, xpath)
            for link in links:
                try:
                    href = link.get_attribute('href')
                    if href and href.startswith(url_base):
                        print(f"Intentando hacer clic en el enlace: {href}")
                        # Usa execute_script para hacer clic en el enlace
                        self.driver.execute_script("arguments[0].click();", link)
                        print(f"Enlace clickeado: {href}")
                        time.sleep(30)  # Espera 60 segundos antes de iniciar la próxima ronda
                        print('scorll en la pagina')
                        self.scroll_down()
                        found_link = True
                        break  # Sale del bucle si se hace clic en un enlace
                except Exception as e:
                    print(f"No se pudo hacer clic en el enlace: {e}")
            if found_link:
                break  # Sale del bucle principal si se ha hecho clic en un enlace
        
        if not found_link:
            # Si no se encuentra el enlace, hacer scroll hacia abajo
            self.scroll_down()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print("Se realizó scroll hacia abajo en la página.")

    def close(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
