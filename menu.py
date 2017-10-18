# -*- coding: utf-8 -*-


def factorial():
    """Factorial"""
    factor = input("Ingresa el valor\n")
    number = factor
    acom = 1

    while factor > 0:
        acom *= factor
        factor -= 1

    print ">>> El factorial de {} es: {} ".format(number, acom)

def sum_sucesiva():
    """Suma sucesiva"""
    number = input("Escribe el valor hasta donde deseas sumar\n")
    result = (number * (number + 1))/2

    print ">>> La suma sucesiva de 1 a {} es: {} ".format(number, result)

def binario():
    """convertir a binario"""
    num = input("Escribe el valor que deseas convertir\n")
    number = num
    binary = ''

    while num // 2 != 0:
        binary = str(num % 2) + binary
        num = num // 2

    result = str(num) + binary
    print ">>> El número binario de {} es {}".format(number, result)



if __name__ == '__main__':
    end_up = False
    option = 'Escribe la opción que deseas'

    menu = {'a': factorial, 'b': sum_sucesiva, 'c': binario}

    while not end_up:
        print('=' * len(option))
        print(option)
        print('=' * len(option))

        for opcion, function in menu.iteritems():
            message = '{}) {}'.format(opcion, function.__doc__)
            print(message)

        value_answer = str(raw_input('\nOpción : ').lower())
        end_up = value_answer == 'terminar'

        tarea = menu.get(value_answer,None)
        if tarea:
            tarea()

    else:
        print("Hemos terminado nuestra tarea,\nHasta pronto")
