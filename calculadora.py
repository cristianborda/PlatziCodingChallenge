def main(operation):

if __name__ == '__main__':
    print(
    '''
    -------------  CALCULADORA  -------------
        Digita la operacion que deseas implementar

            [ + ] ......  Suma o Adición
            [ - ] ......  Resta o Sustracción
            [ * ] ....... MUltiplicación o Producto
            [ / ] ....... División o Cociente
    ''')   
    operation = str(input('Ingresa la operación que deseas realizar en la caluladora:'))
    main()
    number1 = float(input('Digita el primer numero: '))
    number2 = float(input('Digita el segundo numero:'))
