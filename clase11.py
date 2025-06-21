
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b  


def operacion():

    primer_opcion = float(input("Ingresa el primer numero: "))
    segunda_opcion = float(input("Ingresa el segundo numero: "))
    op = input("Ingresa la operacion, (+, - , *, /):")
    

#-------
    if op  == "+":
     resultado=suma(primer_opcion, segunda_opcion)
     print("el resultado es: ", resultado)
    elif op  == "-":
     resultado=resta(primer_opcion, segunda_opcion)
     print("el resultado es: ", resultado)
    elif op  == "*":
     resultado=multiplicacion(primer_opcion, segunda_opcion)
     print("el resultado es: ", resultado)
    elif op  == "/":
     resultado=division(primer_opcion, segunda_opcion)
     print("el resultado es: ", resultado)
    else:
        print("Error operacion no valida")
    


operacion()


