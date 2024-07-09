# Parcial 1 Juan Manuel Bravo comision 311: #

def validar_nombre(nombre):
    if nombre.isalpha() and nombre.istitle() and len(nombre)<= 20:
        return nombre
    else:
        print("Nombre o apellido invalidos, debe empezar en mayuscula y tener menos de 20 caracteres")
        
def validar_apellido(apellido):
    if apellido.isalpha() and apellido.istitle() and len(apellido)<= 20:
        return apellido
    else:
        print("Nombre o apellido invalidos, debe empezar en mayuscula y tener menos de 20 caracteres")

    
        
def validar_edad(edad):
    if edad.isdigit() and 1 <= int(edad) <= 120:
        return int(edad)
    else:
        print("Edad invalida, ingrese un rango entre 1 y 120")
                
def validar_altura(altura):
    if altura.isdigit() and 30 <= int(altura) <= 230:
        return int(altura)
    else:
        print("Altura invalida, debe ser entre 30 y 230 cms")
        
def validar_dni(dni):
    if dni.isdigit() and len(dni) == 8 and 4000000 <= int(dni) <= 99999999:
        return dni
    else:
        print("DNI invalido, debe tener 8 digitos y entrar entre 4000000 y 99999999")
        
def validar_peso(peso):
    peso_float = float(peso)
    if 10 <= peso_float <= 300:
        return peso_float
    else:
        print("Peso invalido debe de estar entre 10 y 300 kgs")
        
def validar_gruposanguineo(grupo_sanguineo):
    grupos_validos = ["A+", "A-", "B+" , "B-", "AB+", "AB-", "0+","0-"]
    if grupo_sanguineo in grupos_validos:
        return grupo_sanguineo
    else:
        print("Su grupo sanguineo es invalido")
        
def solicitar_datos_pte():
    nombre = validar_nombre(input("Ingrese el nombre del paciente "))
    apellido =validar_apellido(input("Ingrese el apellido del paciente "))
    edad = validar_edad(input("Ingrese la edad del paciente "))
    altura = validar_altura(input("Ingrese la altura del paciente "))
    peso = validar_peso(input("Ingrese el peso del paciente "))
    dni = validar_dni(input("Ingrese el dni del paciente "))
    grupo_sanguineo = validar_gruposanguineo(input("Ingrese el grupo sanguineo del paciente "))
    return nombre, apellido, edad, altura, peso, dni, grupo_sanguineo

def obtener_criterio_orden():
    print("\nCriterios de ordenación:")
    print("a. Nombre")
    print("b. Apellido")
    print("c. Altura")
    print("d. Grupo sanguíneo")
    while True:
        criterio = input("Seleccione un criterio de ordenación: ").lower()
        if criterio in ['a', 'b', 'c', 'd']:
            return criterio
        else:
            print("Opción no válida.")


