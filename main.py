import threading
import random
from bot.bot import Bot  # Asegúrate de que esta importación sea correcta para tu estructura de proyecto
from controller.request import obtener_datos_endpoint 
import time

def ejecutar_bots():
    datos_endpoint = obtener_datos_endpoint()

    # Reemplaza marcas_de_carros por las keywords obtenidas del endpoint
    all_keywords = [item['keywords'][0] for item in datos_endpoint if 'keywords' in item and item['keywords']]
    random.shuffle(all_keywords)
    keywords_de_carros = all_keywords[:5]
    print(keywords_de_carros)

    # Lee los proxies del archivo
    with open('proxys/proxies.txt', 'r') as file:
        proxies = file.read().splitlines()

    lista_negra_proxies = set()  # Se inicia con una lista vacía cada vez que se llama a la función

    lock = threading.Lock()

    def obtener_proxy_no_utilizado():
        with lock:
            proxy_aleatorio = random.choice(proxies)
            proxy_ip = proxy_aleatorio.split(';')[0]
            intentos = 0  # Evita un bucle infinito
            while proxy_ip in lista_negra_proxies and intentos < len(proxies):
                proxy_aleatorio = random.choice(proxies)
                proxy_ip = proxy_aleatorio.split(';')[0]
                intentos += 1
            if intentos >= len(proxies):
                return None
            lista_negra_proxies.add(proxy_ip)
            return proxy_ip

    def start_bot_in_thread(query):
        proxy = obtener_proxy_no_utilizado()
        if proxy:
            bot = Bot(proxy=proxy)
            bot.open_page()
            bot.search(query)
            bot.close()
        else:
            print(f"No se encontró proxy disponible para {query}.")

    threads = []

    for marca in keywords_de_carros:
        t = threading.Thread(target=start_bot_in_thread, args=(marca,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    # Se elimina el código para guardar la lista negra, ya que no se requiere

    print("Lista negra de proxies utilizados en esta ejecución:")
    for proxy in lista_negra_proxies:
        print(proxy)

# Bucle infinito para ejecutar los bots continuamente
while True:
    ejecutar_bots()
    print("Esperando antes de iniciar la próxima ronda...")
    time.sleep(10)  # Ajusta este tiempo según necesites, aquí se ha dejado en 10 segundos para el ejemplo
