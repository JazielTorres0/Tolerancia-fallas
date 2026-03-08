import subprocess
import time
from logger import log_event

def iniciar_servicio():
    log_event("Iniciando servicio principal...")
    return subprocess.Popen(["python", "servicio_principal.py"])

def monitor():
    proceso = iniciar_servicio()

    while True:
        time.sleep(10)

        if proceso.poll() is not None:
            log_event("Servicio caído. Reiniciando...")
            proceso = iniciar_servicio()
        else:
            log_event("Servicio activo")

if __name__ == "__main__":
    log_event("Demonio monitor iniciado")
    monitor()