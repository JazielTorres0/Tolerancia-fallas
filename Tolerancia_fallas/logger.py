from datetime import datetime

LOG_FILE = "eventos.log"

def log_event(mensaje):
    tiempo = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    linea = f"[{tiempo}] {mensaje}"

    print(linea)

    with open(LOG_FILE, "a") as f:
        f.write(linea + "\n")