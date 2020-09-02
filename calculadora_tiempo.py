def main(option):
    if option == 'a':
        hours = int(input('Introduce la cantidad de horas que quieres convertir a segundos: '))
        hours_in_seconds = hours* 3600
        print(f'{hours} hora(s) equivalen a: {hours_in_seconds} segundos')
    elif option == 'b':
        minutes = int(input('Introduce la cantidad de minutos que quieres convertir a segundos: '))
        minutes_in_seconds = minutes * 60
        print(f'{minutes} minuto(s) equivalen a: {minutes_in_seconds} segundos')
    else:
        hours = int(input('Introduce la cantidad de horas que quieres convertir a segundos: '))
        minutes = int(input('Introduce la cantidad de minutos que quieres convertir a segundos: '))
        hours_minutes_in_seconds = hours* 3600 + minutes * 60
        print(f'{hours} hora(s) y {minutes} minuto(s) equivalen a: {hours_minutes_in_seconds} segundos')

 
if __name__ == '__main__':
    print(
    '''
    BIENVENIDO A LA CALCULADORA DE SEGUNDOS
    
    OPCIONES DISPONIBLES:
     
            a) Expresion de horas a segundos
            b) Expresión de minutos a segundos
            c) Expresion de horas y minutos a segundos
    ''')
    option = str(input('Ingresa la opción que más se adecue a tu solicitud: '))
    main(option)
  