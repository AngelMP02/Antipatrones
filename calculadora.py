#creamos funciones para cada operacion
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("No se puede dividir entre cero.") 
def calcular(operacion, num1, num2):
    if operacion == 'suma':
        return suma(num1, num2)
    elif operacion == 'resta':
        return resta(num1, num2)
    elif operacion == 'multiplicacion':
        return multiplicacion(num1, num2)
    elif operacion == 'division':
        return division(num1, num2)
    else:
        raise ValueError("Operación no soportada.")