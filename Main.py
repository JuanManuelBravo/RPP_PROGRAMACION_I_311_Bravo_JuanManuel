# Parcial 1 Juan Manuel Bravo comision 311: #
from inputs import *
from pacientes import *

archivo = open("pacientes.csv","w")



def menudeapp():
    pacientes = [
        Paciente(1,"Juan","Bravo",28,170,95,"39208990","A+"),
        Paciente(2,"Matias","Alvarez",19,180,80,"39244134","0+"),
        Paciente(3,"German","Gonzalez",20,195,90,"39244264","A-"),
        Paciente(4,"Utn","Avellaneda",28,178,100,"39244334","AB+")
    ]
    
    while True:
        print("Menu:")
        print("1. Dar de alta")
        print("2. Modificar")
        print("3. Eliminar")
        print("4. Mostrar todos")
        print("5. Ordenar pacientes")
        print("6. Buscar paciente por DNI")
        print("7. Calcular promedio")
        print("8. Indicar compatibilidad sanguinea")
        print("9. Salir")
        opcion = input("Selecciona una opcion para continuar.")
        
        
        match opcion:
            
            case '1':
                dar_de_alta(pacientes)
            case '2':
                modificar_paciente(pacientes)
            case '3':
                eliminar_paciente(pacientes)
            case '4':
                mostrar_todos(pacientes)
            case '5':
                criterio = obtener_criterio_orden()
                ascendente = input("Orden ascendente? (s/n): ").lower() == 's'
                ordenar_pacientes(pacientes, criterio, ascendente)
                mostrar_todos(pacientes)
            case '6':
                buscar_paciente_dni(pacientes)
            case '7':
                calcular_promedio(pacientes)
            case '8':
                dni = input("Ingrese el DNI del paciente para determinar compatibilidad: ")
                indicar_compatibilidad(pacientes, dni)
        
            case '9':
                completar_csv("pacientes.csv",pacientes)
                print("Datos guardados. Saliendo del programa.")
                break
                    
menudeapp()