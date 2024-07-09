# Parcial 1 Juan Manuel Bravo comision 311: #
from inputs import *
import csv

 



def dar_de_alta(pacientes):
    nombre, apellido, edad, altura, peso, dni, grupo_sanguineo = solicitar_datos_pte()
    nuevo_paciente = Paciente(Paciente.id_contador, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo)
    pacientes.append(nuevo_paciente)
    Paciente.id_contador += 1
    print(f"Paciente {nombre} {apellido} ha sido dado de alta con ID {nuevo_paciente.id}.")
        
def modificar_paciente(pacientes):
        dni = validar_dni(input("Ingrese el DNI del paciente"))
        for paciente in pacientes:
            if paciente.dni == dni:
                print("Paciente encontrado. seleccione dato a modificar:")
                print("1. Nombre")
                print("2. Apellido")
                print("3. Edad")
                print("4. Altura")
                print("5. Peso")
                print("6. Grupo sanguineo")
                opcion = input("Seleccione una opcion:")
                if opcion == "1":
                    paciente.nombre = validar_nombre(input("Ingrese el nuevo nombre: "))
                elif opcion == "2":
                    paciente.apellido = validar_apellido(input("Ingrese nuevo apellido "))
                elif opcion == "3":
                    paciente.edad = validar_edad(input("Ingrese nueva edad "))
                elif opcion == "4":
                    paciente.altura = validar_altura(input("Ingrese nueva altura "))
                elif opcion == "5":
                    paciente.peso = validar_peso(input("Ingrese nuevo peso "))
                elif opcion == "6":
                    paciente.grupo_sanguineo = validar_gruposanguineo(input("Ingrese el nuevo grupo sanguineo "))
                else:
                    print("opcion invalida")
                    
def eliminar_paciente(pacientes):
        dni = validar_dni(input("Ingrese el DNI del paciente a eliminar:"))
        for paciente in pacientes:
            if paciente.dni == dni:
                pacientes.remove(paciente)
                print("Paciente eliminado.")
                
def mostrar_todos(pacientes):
        print("*" * 89)
        print("| Nombre       | Apellido     | Edad | Altura | Peso   | DNI       | Grupo sanguíneo |")
        print("-" * 89)
        for paciente in pacientes:
            print(f"| {paciente.nombre:12} | {paciente.apellido:12} | {paciente.edad:4} | {paciente.altura:5} cm | {paciente.peso:6.1f} kg | {paciente.dni:8} | {paciente.grupo_sanguineo:15} |")
        print("*" * 89)
        
def buscar_paciente_dni(pacientes):
        dni = validar_dni(input("Ingrese el DNI"))
        for paciente in pacientes:
            if paciente.dni == dni:
                print(f"Nombre: {paciente.nombre}")
                print(f"Apellido: {paciente.apellido}")
                print(f"Edad: {paciente.edad}")
                print(f"Peso: {paciente.peso}")
                print(f"DNI: {paciente.dni}")
                

             
                
def calcular_promedio(pacientes):
    if not pacientes:
        print("No hay pacientes registrados.")
        return

    while True:
        print("Seleccione el promedio a calcular:")
        print("1. Edad")
        print("2. Altura")
        print("3. Peso")
        print("4. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            promedio = sum(paciente.edad for paciente in pacientes) / len(pacientes)
            print(f"El promedio de edad es: {promedio:.2f} años.")
        elif opcion == "2":
            promedio = sum(paciente.altura for paciente in pacientes) / len(pacientes)
            print(f"El promedio de altura es: {promedio:.2f} cm.")
        elif opcion == "3":
            promedio = sum(paciente.peso for paciente in pacientes) / len(pacientes)
            print(f"El promedio de peso es: {promedio:.2f} kg.")
        elif opcion == "4":
            print("Saliendo del cálculo de promedios.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

def completar_csv(path:str, lista:list):
    with open(path, "w") as archivo:
        for i in lista:
            linea = f"{i}\n"
            archivo.write(linea)
        
def ordenar_pacientes(pacientes, criterio, ascendente):
    criterios = {
        'a': 'nombre',
        'b': 'apellido',
        'c': 'altura',
        'd': 'grupo_sanguineo'
    }
    auxiliar = criterios[criterio]

    n = len(pacientes)
    for i in range(n - 1):
        for j in range(n - i - 1):
            valor_actual = getattr(pacientes[j], auxiliar)
            valor_siguiente = getattr(pacientes[j + 1], auxiliar)
            if (valor_actual > valor_siguiente and ascendente) or (valor_actual < valor_siguiente and not ascendente):
                pacientes[j], pacientes[j + 1] = pacientes[j + 1], pacientes[j]


    

class Paciente:
    id_contador = 1
    def __init__(self, id, nombre, apellido, edad, altura, peso, dni, grupo_sanguineo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.altura = altura
        self.peso = peso
        self.dni = dni
        self.grupo_sanguineo = grupo_sanguineo
        
    def __repr__(self):
        return f"Paciente({self.id}, '{self.nombre}', '{self.apellido}', {self.edad}, {self.altura}, {self.peso}, {self.dni}, '{self.grupo_sanguineo}')"
        
        
    
def indicar_compatibilidad(pacientes, dni):
        
    paciente_elegido = None
    for paciente in pacientes:
        if paciente.dni == dni:
            paciente_elegido = paciente
            break
        
    if paciente_elegido:
        print(f"Grupo sanguíneo del paciente seleccionado: {paciente_elegido.grupo_sanguineo}")
        
        print("\nEl paciente puede recibir sangre de los siguientes grupos:")
        grupo_sanguineo = paciente_elegido.grupo_sanguineo
        
        tabla_compatibilidad = {
            "A+": ["0+", "0-", "A+", "A-"],
            "A-": ["0-", "A-"],
            "B+": ["0+", "0-", "B+", "B-"],
            "B-": ["0-", "B-"],
            "AB+": ["A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-"],
            "AB-": ["AB-", "0-", "A-", "B-"],
            "0+": ["0+", "0-"],
            "0-": ["0-"]
        }
        
        if grupo_sanguineo in tabla_compatibilidad:
            compatibles_recibir = tabla_compatibilidad[grupo_sanguineo]
            print(", ".join(compatibles_recibir))
        else:
            print("No se encontró información de compatibilidad para este grupo sanguíneo.")
        
        print("\nEl paciente puede donar sangre a los siguientes grupos:")
        
        
        tabla_compatibilidad_donar = {
            "A+": ["A+", "AB+"],
            "A-": ["A+", "A-", "AB+", "AB-"],
            "B+": ["B+", "AB+"],
            "B-": ["B+", "B-", "AB+", "AB-"],
            "AB+": ["AB+"],
            "AB-": ["AB+", "AB-"],
            "0+": ["A+", "B+", "AB+", "0+"],
            "0-": ["A+", "A-", "B+", "B-", "AB+", "AB-", "0+", "0-"]
        }
        
        
        if grupo_sanguineo in tabla_compatibilidad_donar:
            compatibles_donar = tabla_compatibilidad_donar[grupo_sanguineo]
            print(", ".join(compatibles_donar))  
        else:
            print("No se encontró información de compatibilidad para determinar donación.")
    
    else:
        print("No se encontró ningún paciente con el DNI ingresado.")
    mostrar_compatibles(pacientes,paciente_elegido)

def mostrar_compatibles(pacientes:list[object],paciente:object):
    if paciente.grupo_sanguineo == "A+":
        for persona in pacientes:
            if persona.grupo_sanguineo == "A+" or persona.grupo_sanguineo == "AB+":
                mostrar_paciente(persona)
    elif paciente.grupo_sanguineo == "A-":
        for persona in pacientes:
            if persona.grupo_sanguineo == "A-" or persona.grupo_sanguineo == "AB+" or persona.grupo_sanguineo == "A+" or persona.grupo_sanguineo == "AB-" :
                mostrar_paciente(persona)
    elif paciente.grupo_sanguineo == "B+":
        for persona in pacientes:
            if persona.grupo_sanguineo == "B+" or persona.grupo_sanguineo == "AB+":
                mostrar_paciente(persona)
    elif paciente.grupo_sanguineo == "B-":
        for persona in pacientes:
            if persona.grupo_sanguineo == "B+" or persona.grupo_sanguineo == "B-":
                mostrar_paciente(persona)
    elif paciente.grupo_sanguineo == "AB+":
        for persona in pacientes:
            if persona.grupo_sanguineo == "AB+":
                mostrar_paciente(persona)
    elif paciente.grupo_sanguineo == "AB-":
        for persona in pacientes:
            if persona.grupo_sanguineo == "AB+" or persona.grupo_sanguineo == "AB-":
                mostrar_paciente(persona)
    elif paciente.grupo_sanguineo == "0+":
        for persona in pacientes:
            if persona.grupo_sanguineo == "A+" or persona.grupo_sanguineo == "B+" or persona.grupo_sanguineo == "AB+" or persona.grupo_sanguineo == "0+" :
                mostrar_paciente(persona)
    elif paciente.grupo_sanguineo == "0-":
        for persona in pacientes:
            if persona.grupo_sanguineo == "A-" or persona.grupo_sanguineo == "A+" or persona.grupo_sanguineo == "B+" or persona.grupo_sanguineo == "B-" or persona.grupo_sanguineo == "AB-" or persona.grupo_sanguineo == "AB+" or persona.grupo_sanguineo == "0-" or persona.grupo_sanguineo == "0+" :
                mostrar_paciente(persona)
        
        
        
        
                
                

def mostrar_paciente(paciente:object):
    print(f"| {paciente.nombre:<10} | {paciente.apellido:<12} | {paciente.edad:<6} | {paciente.altura:<7} cm | {paciente.peso:<6}kg | {paciente.dni:08} | {paciente.grupo_sanguineo:<20}|")
    print("***")
    
def calcular_imc(paciente):
    altura_metros = paciente.altura / 100  
    return paciente.peso / (altura_metros ** 2)

def obtener_matriz(pacientes):
    grupos_sanguineos = {
        'A+': [],
        'A-': [],
        'B+': [],
        'B-': [],
        'AB+': [],
        'AB-': [],
        '0+': [],
        '0-': []
    }
    
    
    for paciente in pacientes:
        grupos_sanguineos[paciente.grupo_sanguineo].append(paciente)
    
    matriz = []
    
    for grupo, pacientes_grupo in grupos_sanguineos.items():
        if pacientes_grupo:
            alturas = [p.altura for p in pacientes_grupo]
            edades = [p.edad for p in pacientes_grupo]
            imcs = [calcular_imc(p) for p in pacientes_grupo]
            
            altura_promedio = sum(alturas) / len(alturas)
            edad_maxima = max(edades)
            imc_promedio = sum(imcs) / len(imcs)
            
            matriz.append([grupo, altura_promedio, edad_maxima, imc_promedio])
        else:
            matriz.append([grupo, 0, 0, 0])
    
    return matriz

def mostrar_matriz(matriz):
    print("***************************************************************")
    print("| Grupo Sanguíneo | Altura Promedio | Edad Máxima | IMC Promedio |")
    print("---------------------------------------------------------------")
    for fila in matriz:
        grupo, altura_promedio, edad_maxima, imc_promedio = fila
        print(f"| {grupo:<15} | {altura_promedio:<15.2f} cm | {edad_maxima:<11} | {imc_promedio:<11.2f} |")
    print("***************************************************************")