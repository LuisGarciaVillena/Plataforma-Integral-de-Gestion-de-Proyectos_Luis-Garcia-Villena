#!/usr/bin/env python3

import os
import subprocess

# Lista de servicios críticos a monitorear
SERVICES = ["apache2", "postgresql"]

# Función para verificar el estado del servicio
def check_service(service):
    try:
        # Verificar el estado del servicio usando systemctl
        status_output = subprocess.check_output(["systemctl", "is-active", service])
        if status_output.strip() == b"active":
            print(f"{service} está corriendo.")
            return True
        else:
            print(f"{service} no está corriendo.")
            return False
    except subprocess.CalledProcessError:
        print(f"No se pudo verificar el estado de {service}.")
        return False

# Función para reiniciar el servicio
def restart_service(service):
    try:
        subprocess.check_call(["sudo", "systemctl", "restart", service])
        print(f"{service} ha sido reiniciado.")
    except subprocess.CalledProcessError as e:
        print(f"Error al reiniciar {service}: {e}")

# Función principal para monitorear y reiniciar servicios
def monitor_services():
    for service in SERVICES:
        if not check_service(service):
            print(f"Intentando reiniciar {service}...")
            restart_service(service)

if __name__ == "__main__":
    monitor_services()
