from funciones import *

print('\n Mini-Calculadora \n')
while True:
    mostrar_menu()    
    respuesta = input('Elija una opción: (1/2/3/4/5) ')

    if respuesta == '5':
        print('Saliendo...')
        break
    
    if respuesta in ['1','2','3','4']:
        num1 = float(input('Ingrese el primer número: '))
        num2 = float(input('Ingrese el segundo número: '))
    
        if respuesta == '1':
            print(f'{num1} + {num2} = {suma(num1, num2)}')
        elif respuesta == '2':
            print(f'{num1} - {num2} = {resta(num1, num2)}')
        elif respuesta == '3':
            print(f'{num1} * {num2} = {multiplicacion(num1, num2)}')
        elif respuesta == '4':
            print(f'{num1} / {num2} = {division(num1, num2)}')
        else:
            print('Opción invalida. Intentelo nuevamente')


