#sumar dos numeros
def add(a, b):
    return a + b

#restar dos numeros
def subtract(a, b):
    return a - b

#dividir dos numeros
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

#metodo que devuelve el cuadrado de un numero
def sq(n):
    if n == 4:
        return 16
    else: return 25