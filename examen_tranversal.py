from random import randint
from statistics import mean,geometric_mean

nombres = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
trabajador=[]
def asignar_sueldos():
    for nombre in nombres:
        trabajador.append({"nombre":nombre,"Sueldos":randint(300000,2500000)})
    print("-"*30)
    for i in range(len(trabajador)):
        print(f"{i+1} - {trabajador[i]}")
        print("-"*30)
def clasificar_sueldos():
    for i in trabajador:
        if i["Sueldos"] < 800000:
            print(f"Sueldos menores a $800.000 Total\n{i}")
        elif i["Sueldos"] >= 800000 and i["Sueldos"] < 2000000:
            print(f"Sueldos entre $800.000 y $2.000.000 Total\n{i}")
        elif i["Sueldos"] > 2000000:
            print(f"Sueldos superior a $2.000.000 Total\n{i}")
def estadisticas():
    for i in trabajador:
        geo=geometric_mean([i["Sueldos"]])
        m_max=max([i["Sueldos"]])
        n_min=mean([i["Sueldos"]])
        print(f"numero maximo{m_max}")
        print(f"numero minimo{n_min}")
        print(f"numero geo{geo}")
def reporte_sueldo():
    print("En proceso!!")    
def menu():
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas.")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
   
while True:
    menu()
    opc=input("Ingrese una opción:  ")
    if opc=="1":
        asignar_sueldos()
    elif opc=="2":
        clasificar_sueldos()   
    elif opc=="3": 
        estadisticas()       
    elif opc=="4":
        reporte_sueldo()      
    elif opc=="5":
        print("Finalizando programa…\nDesarrollado por Sebastian Orellana Balbi\nRUT 20.311.148-7")
        break         