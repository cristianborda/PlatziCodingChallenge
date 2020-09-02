def main(word, times):
        for _ in range(1, times +1):
            print(word)
    

if __name__ == '__main__':
    word = str(input('Ingresa la palabra que deseas repetir: '))
    times = int(input('Cuantas veces quieres repetir la palabra anterior: '))
    print('***----****')
    main(word,times)
    print('***----****')
   
    