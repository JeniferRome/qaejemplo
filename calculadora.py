# Calculadora basica en Python
a = 2
b = 1

# Función para sumar
def sumar(a, b):
    return a + b
resultado_suma = sumar(a,b)
print("Resultado de la suma:", resultado_suma)


# Función para restar
def restar(a, b):
    return a - b
resultado_restar = restar(a,b)
print("Resultado de la resta:", resultado_restar)

# Función para multiplicar
def multiplicar(a, b):
    return a * b
resultado_multiplicacion = multiplicar(a,b)
print("Resultado de la multiplicacion:", resultado_multiplicacion)

# Función para dividir
def dividir(a, b):
    if b == 0:
        return "Error: No se puede dividir entre cero"
    return a / b

def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Error: No se puede dividir entre cero"
    except TypeError:
        return "Error: Tipos de datos no válidos (deben ser números)"
    except Exception as e:
        return f"Ocurrió un error inesperado: {e}"
    
    
# Pruebas
print("Resultado de division Ok:", dividir(a, b))   # Salida: 5.0
print("Resutlatdo de division entre 0:", dividir(a, 0))  # Salida: Error: No se puede dividir entre cero
print("Resultado de division entre letra:", dividir(a, "a")) # Salida: Error: Tipos de datos no válidos (deben ser números)