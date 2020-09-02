def wordreverse(s):
    if s == "":
        return s
    else:
        return (wordreverse(s[1:]) + s[0])
    
if __name__ == '__main__':
    s = input('Escribe la oración que deseas voltear: ')
    wordreverse(s)
    print(f'La oración {s} volteada queda: {wordreverse(s)}')

    
