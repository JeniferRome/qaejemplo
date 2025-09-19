def Sumar(a, b):
    return a + b

def Restar(a, b):
    return a - b

def Multiplicar(a, b):
    return a * b

def Dividir(a, b):
    try:
       return a / b 
    except ZeroDivisionError:
        return "Error no se puede dividir entre cero"
    
    def calculadora():
        print("Bienvenido a la calculadora Lineal")

        try: 
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))
        except ValueError:
            print("Error debes ingresar un numero valido")
            return # termina la funcion si hay error en la entrada
        
        print("Operaciones disponibles: sumar, restar, multiplicar, dividir")
        operacion = input("Elige una operacion: ")

        if operacion == "sumar":
           resultado = sumar(num1, num2)
        elif operacion == "restar":
            resultado = restar(num1, num2)
        elif operacion == "multiplicar":
            resultado = Multiplicar(num1, num2)
        elif operacion == "dividir":
            resultado = Dividir(num1, num2)
        else:
            print("Error: Operacion no valida")
            return
    
    print(f"El resultado de {operacion] es: {resultado]")