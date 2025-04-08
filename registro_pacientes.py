from datetime import datetime

# Diccionario para almacenar pacientes
pacientes = {}

# Función para registrar paciente
def registrar_paciente():
    nombre = input("Nombre del paciente: ")
    edad = input("Edad: ")
    diagnostico = input("Diagnóstico: ")

    if nombre not in pacientes:
        pacientes[nombre] = {
            "edad": edad,
            "diagnóstico": diagnostico,
            "sesiones": []
        }
        print(f"✅ Paciente {nombre} registrado.")
    else:
        print(f"⚠ El paciente {nombre} ya existe.")

# Función para registrar una sesión
def registrar_sesion():
    nombre = input("Nombre del paciente: ")
    if nombre not in pacientes:
        print("❌ El paciente no está registrado.")
        return

    fecha = input("Fecha de sesión (YYYY-MM-DD): ")
    actividad = input("Actividad realizada: ")
    observaciones = input("Observaciones: ")

    pacientes[nombre]["sesiones"].append({
        "fecha": fecha,
        "actividad": actividad,
        "observaciones": observaciones
    })

    print("📌 Sesión registrada correctamente.")

# Función para mostrar los datos registrados
def mostrar_pacientes():
    for nombre, datos in pacientes.items():
        print(f"\n🧑‍🦳 Paciente: {nombre} | Edad: {datos['edad']} | Dx: {datos['diagnóstico']}")
        for sesion in datos["sesiones"]:
            print(f"  📅 {sesion['fecha']} | {sesion['actividad']} | {sesion['observaciones']}")

# Menú principal
def menu():
    while True:
        print("\n=== Registro de Pacientes - Terapia Ocupacional ===")
        print("1. Registrar nuevo paciente")
        print("2. Registrar sesión")
        print("3. Mostrar pacientes y sesiones")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            registrar_paciente()
        elif opcion == "2":
            registrar_sesion()
        elif opcion == "3":
            mostrar_pacientes()
        elif opcion == "4":
            print("👋 Saliendo del sistema.")
            break
        else:
            print("❌ Opción no válida.")

# Ejecutar
menu()



