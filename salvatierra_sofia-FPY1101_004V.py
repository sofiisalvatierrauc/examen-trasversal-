import statistics
import csv
import random

trabajadores = [
    {"nombre": "Juan Pérez", "ocupacion": "programador"},
    {"nombre": "María García", "ocupacion": "Analista"},
    {"nombre": "Carlos López", "ocupacion": "Programador"},
    {"nombre": "Ana Martínez", "ocupacion": "Jefe de Proyecto"},
    {"nombre": "Pedro Rodríguez", "ocupacion": "Consultor TI"},
    {"nombre": "Laura Hernández", "ocupacion": "Analista"},
    {"nombre": "Miguel Sánchez", "ocupacion": "Programador"},
    {"nombre": "Isabel Gómez", "ocupacion": "analista"},
    {"nombre": "Francisco Díaz", "ocupacion": "Consultor TI"},
    {"nombre": "Elena Fernández", "ocupacion": "consultor"}
]
    
def asignar_sueldo_aleatorio():
    for empleado in trabajadores:
        empleado ["sueldo"]=random.randint(300000, 2500000)

def clasificar_sueldos():
    for empleado in trabajadores:
        nombre= empleado["nombre"]
        sueldo= empleado["sueldo"]
        if sueldo < 800000:
            print(f"{nombre}: {empleado['ocupacion']}, ${sueldo} - Sueldo bajo")
        elif 800000 <= sueldo <= 2000000:
            print(f"{nombre}: {empleado['ocupacion']}, ${sueldo} - sueldo medio")
        else:
            print(f"{nombre}: {empleado['ocupacion']}, ${sueldo} - sueldo alto")
            
def ver_estadisticas():
    sueldos= [empleado["sueldo"] for empleado in trabajadores]
    sueldo_maximo= max(sueldos)
    sueldo_minimo= min(sueldos)
    promedio_sueldo= statistics.mean(sueldos)
    medida_G= statistics.geometric_mean(sueldos)

    print("estadisticas de sueldos: ")
    print(f"sueldo mas alto: ${sueldo_maximo}")
    print(f"suelgo mas bajo: ${sueldo_minimo}")
    print(f"promedio de sueldos: ${promedio_sueldo}")
    print(f"medida geometria de sueldos: ${medida_G}")

def reporte_de_sueldos():
    nombre_archivo= "reporte_del_sueldo.csv"
    with open(nombre_archivo, mode='w', newline="") as file:
         writer= csv.writer(file)
         writer.writerow(['nombre', 'cargo', 'sueldo_base', 'descuento_salud', 'descuento_afp', 'sueldo_liquido'])
    for empleado in trabajadores:
            nombre=empleado['nombre']
            ocupacion= empleado['ocupacion']
            sueldo_base= empleado['sueldo']
            descuento_salud= sueldo_base * 0.07
            descuento_AFP= sueldo_base * 0.12
            sueldo_liquido= sueldo_base - descuento_salud - descuento_AFP
           
            print(f"\nNombre empleado: {nombre} ocupacion: {ocupacion} Sueldo Base: ${sueldo_base} Descuento Salud: ${descuento_salud} Descuento AFP: ${descuento_AFP} Sueldo Líquido: ${sueldo_liquido}")
while True:
    print("**Menu**")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadisticas")
    print("4. Generar reporte de sueldos")
    print("5. Salir del programa")

    opcion=input("seleccione una opcion:")
    
    if opcion == "1":
        asignar_sueldo_aleatorio()
        print("su sueldo fue asignado correctamente")
    elif opcion =="2":
        clasificar_sueldos()
    elif opcion =="3":
        ver_estadisticas()
    elif opcion =="4":
        reporte_de_sueldos()
    elif opcion =="5":
        print("Finalizando el programa")
        print("desarrollado por: Sofia Salvatierra Salvatierra")
        print("Rut: 22.072.26-3")
        break
    else:
        print("opcion no valida, vuelva a intentarlo.")       

       
