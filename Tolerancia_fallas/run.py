import subprocess

print("Iniciando monitor del sistema...")

subprocess.Popen(["python", "monitor_demonio.py"])

print("Monitor ejecutándose en segundo plano")