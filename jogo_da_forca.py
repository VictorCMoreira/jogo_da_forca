class JogoDaForca:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_corretas = set()
        self.letras_erradas = set()
        self.max_tentativas = 6
        self.indice_grafico = 0
        self.grafico = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

    def adivinhar_letra(self, letra):
        if letra in self.palavra:
            self.letras_corretas.add(letra)
            if self.venceu():
                self.status()
        else:
            self.letras_erradas.add(letra)
            self.indice_grafico += 1
            if len(self.letras_erradas) >= self.max_tentativas:
                self.status()

    def jogo_terminado(self):
        return self.venceu() or len(self.letras_erradas) >= self.max_tentativas

    def venceu(self):
        return set(self.palavra) == self.letras_corretas

    def board(self):
        board = ''
        for letra in self.palavra:
            if letra in self.letras_corretas:
                board += letra + ' '
            else:
                board += '_ '
        return board.strip()

    def status(self):
        print(self.grafico[self.indice_grafico])
        print(f'Palavra: {self.board()}')
        print(f'Letras corretas: {", ".join(sorted(self.letras_corretas))}')
        print(f'Letras erradas: {", ".join(sorted(self.letras_erradas))}')
        print(f'Tentativas restantes: {self.max_tentativas - len(self.letras_erradas)}')


def main():
    import random
    lista_de_palavras = open("palavras.txt", "r").read().split(", ")
    palavra = random.choice(lista_de_palavras)
    
    jogo = JogoDaForca(palavra)
    while not jogo.jogo_terminado():
        jogo.status()
        letra = input("Digite uma letra: ").lower()
        jogo.adivinhar_letra(letra)
    
    if jogo.venceu():
        print("Parabéns, você venceu!")
    else:
        print("Que pena, você perdeu. A palavra era:", jogo.palavra)

if __name__ == "__main__":
    main()