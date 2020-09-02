def main(text):
    vocales = ['a','á', 'e', 'é', 'i', 'í', 'o', 'ó', 'u', 'ú']
    consonantes = ['q', 'c', 'l', 'd', 'v']
    for i in range(len(text)):
        if text[i] == vocales[0] or text[i] == vocales[1]:
            text[i] = consonantes[0]
        if text[i] == vocales[2] or text[i] == vocales[3]:
            text[i] = consonantes[1]
        if text[i] == vocales[4] or text[i] == vocales[5]:
            text[i] = consonantes[2]
        if text[i] == vocales[6]or text[i] == vocales[7]:
            text[i] = consonantes[3]
        if text[i] == vocales[8] or text[i] == vocales[9]:
            text[i] = consonantes[4]
   
    return ("".join(text))


if __name__ == '__main__':
    text = list(input('Ingresa el texto donde quieres reemplazar vocales por consonantes: '))
    print('')
    print('-*-*-*-*-*-*-*-*' * 9)
    print('')
    print(main(text))
    print('')
    print('-*-*-*-*-*-*-*-*' * 9)
