import time
import random
import signal
import sys
from logger import log_event

running = True

def detener_servicio(signum, frame):
    global running
    log_event("Señal de cierre recibida. Apagando servicio...")
    running = False

signal.signal(signal.SIGTERM, detener_servicio)
signal.signal(signal.SIGINT, detener_servicio)

def ejecutar_servicio():
    log_event("Servicio principal iniciado")

    while running:
        time.sleep(5)

        # Simulación de falla
        if random.random() < 0.2:
            log_event("ERROR: El servicio falló inesperadamente")
            sys.exit(1)

        log_event("Servicio funcionando correctamente")

    log_event("Servicio detenido correctamente")

if __name__ == "__main__":
    ejecutar_servicio()