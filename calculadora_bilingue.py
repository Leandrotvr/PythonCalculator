def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def main():
    print("Seleccione el idioma / Select Language:")
    print("1. Español")
    print("2. English")

    idioma = input("Ingrese el número del idioma / Enter the language number (1/2): ")

    if idioma == '1':
        print("Bienvenido a la calculadora básica")
        operaciones = ["Suma", "Resta", "Multiplicación", "División"]
        mensaje_salida = "Saliendo de la calculadora."
        mensaje_error = "Opción no válida. Intenta nuevamente."
    elif idioma == '2':
        print("Welcome to the basic calculator")
        operaciones = ["Addition", "Subtraction", "Multiplication", "Division"]
        mensaje_salida = "Exiting the calculator."
        mensaje_error = "Invalid option. Please try again."
    else:
        print("Opción no válida / Invalid option.")
        return

    print("Seleccione la operación / Select the operation:")
    for i, op in enumerate(operaciones, start=1):
        print(f"{i}. {op}")

    while True:
        opcion = input("Ingrese el número de la operación (1/2/3/4) o 'q' para salir: ")

        if opcion == 'q':
            print(mensaje_salida)
            break

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingrese el primer número / Enter the first number: "))
                num2 = float(input("Ingrese el segundo número / Enter the second number: "))

                if opcion == '1':
                    resultado = suma(num1, num2)
                    print(f"{num1} + {num2} = {resultado}" if idioma == '2' else f"{num1} + {num2} = {resultado}")
                elif opcion == '2':
                    resultado = resta(num1, num2)
                    print(f"{num1} - {num2} = {resultado}" if idioma == '2' else f"{num1} - {num2} = {resultado}")
                elif opcion == '3':
                    resultado = multiplicacion(num1, num2)
                    print(f"{num1} * {num2} = {resultado}" if idioma == '2' else f"{num1} * {num2} = {resultado}")
                elif opcion == '4':
                    resultado = division(num1, num2)
                    print(f"{num1} / {num2} = {resultado}" if idioma == '2' else f"{num1} / {num2} = {resultado}")
            except ValueError:
                print("Por favor, ingresa un número válido. / Please enter a valid number.")
        else:
            print(mensaje_error)

if __name__ == "__main__":
    main()
