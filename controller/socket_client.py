import asyncio
import socketio
from controller.control_bot import start_bot, stop_bot

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Conexión establecida con el servidor de Socket.IO")

@sio.on('start_speed_bot', namespace='/pageSpeed')
async def on_start_bot():
    print("Comando recibido: Iniciar bot")
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, start_bot)

@sio.on('stop_speed_bot', namespace='/pageSpeed')
async def on_stop_bot():
    print("Comando recibido: Detener bot")
    await stop_bot()

@sio.event
async def disconnect():
    print("Desconectado del servidor de Socket.IO")

async def run_sockets():
    try:
        await sio.connect('http://localhost:7182', namespaces=['/pageSpeed'])
        await sio.wait()
    except KeyboardInterrupt:
        print("Programa interrumpido por el usuario")
    finally:
        await sio.disconnect()