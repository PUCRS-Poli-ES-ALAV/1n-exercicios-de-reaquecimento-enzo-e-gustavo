def multiplicacao(num1, num2, mult):
    if mult == 1:
        print(num1)
        return num1
    num1 += num2
    mult -= 1
    multiplicacao(num1, num2, mult)

def inversao(string, inversa):
    tamanho = len(string)
    if tamanho <= 0:
        inversa = "".join(inversa)
        print(inversa)
        return inversa
    inversa.append(string[tamanho - 1])
    inversao(string[:-1], inversa)

def palindromo(string):
    tamanho = len(string)
    if tamanho <= 1:
        print("sim")
        return True
    if string[0] != string[-1]:
        print("não")        
        return None
    palindromo(string[1:-1])

def main():
    multiplicacao(4, 4, 6)
    inversao("string", [])
    palindromo("abaa")
    #ackerman(m, n)

main()