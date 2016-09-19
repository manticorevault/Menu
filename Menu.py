# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 08:06:11 2016

@author: Artur
"""

import random
import time

def main():
    print("\n\n\tEscolha um dos programas que eu já projetei!\n")
    print("\n\t1. O Jogo do Labirinto")
    print("\n\t2. O Jogo da Forca")
    print("\n\t3. O Jogo da Adivinhação de Números")
    print("\n\t4. O Gerador de Nome de Filho")
    print("\n\t5. Sair")

    escolha = int(input("\n\tEscolha um programa! "))
    print("\n\n")
    return escolha
    
def maze():

    print("\nVocê está na porta de um labirinto onde se encontram")
    print("muitos segredos, um tesouro e um terrível monstro")
    print("Sua missão é encontrar o tesouro. Será que irá conseguir?")

    time.sleep(4)

    print("\nVocê entra no labirinto. As paredes estão cheias de mofo.")
    print("O ambiente é frio, o tempo parece ter sido esquecido por lá...")

    time.sleep(3)
    
    print("Você olha para o corredor e...")

    time.sleep(3)

    print("\nExistem dois caminhos. Pela esquerda e pela direita.")
    
    choice = input("Qual caminho você toma? ").lower()
    
    while choice != "direita" and choice != "esquerda":
        choice = input("Qual caminho você toma? ").lower()
        
    caminho = ""
    
    if choice == "direita":
        print("Você segue pela direita, subindo uma escada antiga...")
        time.sleep(3)
        print("No topo da escada, há uma porta velha.")
        print("Você abre cuidadosamente a porta e...")
        caminho = "d1"        
        
    elif choice == "esquerda":
        print("Você segue pela esquerda, descendo uma rampa")
        print("que parece muito traiçoeira...")
        time.sleep(3)
        print("Ao chegar no fim da rampa, você percebe que")
        print("há um pequeno calabouço. Você decide entrar...")
        caminho = "e1"
        
    if caminho == "d1":
        print("A porta no topo da escada abre numa pequena sala oval.")
        print("Lá dentro, há algumas caixas antigas, um baú e...")
        caminho == random.randint(1, 2)
        time.sleep(2)
    elif caminho == "e1":
        print("O calabouço no fim da rampa desce para um pequeno porão.")
        print("Dentro do porão há alguns esqueletos, um arsenal e...")
        caminho == random.randint(1, 2)
        time.sleep(2)
    
    if caminho == 1:
        print("Há uma portinhola atrás de uma mobília antiga")
        time.sleep(2)
        print("Essa portinhola parece levar para uma sala secreta")
        print("atrás da parede...")
        time.sleep(2)
        print("Dentro dessa sala secreta há muito mofo, um punhado")
        print("de peças de armadura antigas e...")
        time.sleep(2)
        caminho = random.randint(1, 2)
    else:
        print("Há um rombo no chão que indica uma passagem")
        time.sleep(2)
        print("Essa passagem parece ter sido esquecida há muito tempo")
        print("pois você sente a espessa poeira em volta dela")
        time.sleep(3)
        print("Ao passar pela passagem, você percebe que há uma")
        print("outra sala, com vários quadros e pinturas e...")
        caminho = random.randint(1, 2)
    
    if caminho == 1:
        print("Outra encruzilhada!")
        time.sleep(2)
        print("Há um caminho de pedra pela direita e outro por uma rampa")
        print("de madeira, à esquerda, levando para uma sala velha...")
        time.sleep(2)
        caminho = input("Qual caminho você toma?")
        while choice != "direita" and choice != "esquerda":
            choice = input("Qual caminho você toma? ").lower()
            
        if caminho == "direita":
            caminho = "d2"
        else:
            caminho = "e2"
    else:
        print("Há entrada (não tão) secreta!")
        time.sleep(2)
        print("Existe um espaço entre a porta e a parede, levando para")
        print("Uma outra sala. Nessa nova sala existem duas portas.")
        time.sleep(2)
        caminho = input("Qual porta você pega?")
        while choice != "direita" and choice != "esquerda":
            choice = input("Qual caminho você toma? ").lower()
        
        if caminho == "direita":
            caminho = "d2"
        else:
            caminho = "e2"
    

    if caminho == "d2":
        print("A nova sala que você entra tem uma série de instrumentos")
        print("musicais antigos, paredes de mármore e...")
        time.sleep(2)
    else:
        print("A nova sala que você entra tem uma estante de livros")
        print("imensa, paredes de marfim e...")
        time.sleep(2)
    
        
    final = random.randint(1, 2)
    if final == 1:
        print("HÁ UM MONSTRO MUITO FEROZ!")
        time.sleep(2)
        print("Você tenta correr, mas o monstro é muito veloz.")
        print("Ele lança suas mãos em volta do seu tornozelo!")
        time.sleep(2)
        print("Você cai, e é devorado pelo monstro!")
        
    else:
        print("HÁ UM TESOURO MUITO LINDO!")
        #time.sleep(2)
        print("Você olha o tesouro, repleto de ouro, jóias e moedas!")
        print("Você percebe que existem muitas riquezas ali dentro,")
        print("E que talvez seja difícil sair daquele labirinto")
        #time.sleep(3)
        print("Mas com muito esforço você consegue se dar bem!")
        
def forca():
    HANGMAN = (
    """

    -----------
    |         |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    |
    -----------
    """,
    """
    -----------
    |         |
    |         O
    |
    |
    |
    |
    |
    |
    |
    |
    |
    -----------
    """,
    """
    -----------
    |         |
    |         O
    |       --+--
    |
    |
    |
    |
    |
    |
    |
    |
    -----------
    """,
    """
    -----------
    |         |
    |         O
    |      /--+--
    |
    |
    |
    |
    |
    |
    |
    |
    -----------
    """,
    """
    -----------
    |         |
    |         O
    |      /--+--/
    |
    |
    |
    |
    |
    |
    |
    |
    -----------
    """,
    """
    -----------
    |         |
    |         O
    |      /--+--/
    |         |
    |         |
    |
    |
    |
    |
    |
    |
    -----------
    """,
    """
    -----------
    |         |
    |         O
    |      /--+--/
    |         |
    |         |
    |         ^
    |        / 
    |       /
    |
    |
    |
    -----------
    """,
    """
    -----------
    |         |
    |         O
    |      /--+--/
    |         |
    |         |
    |         ^
    |        / \
    |       /   \
    |
    |
    |
    -----------
    """)
    
    # Constant to represent the maximum number of wrong guesses a player
    # can take before the game is over. The maximum number of incorrect
    # guesses is one less than the lenght of HANGMAN. This is because 
    # the first image of the empty gallows is displayed even before
    # the player makes a first guess.
    MAX_WRONG = len(HANGMAN) - 1
    
    # Tuple with all the words the computer can pick for the player to
    # guess
    #WORDS = ("PAMONHA", "MEGAZORD", "PRATO DE COMIDA", "PIANO", "MEMPHIS")
    
    # Initialize variables
    #word = random.choice(WORDS) # The word to be guessed /\ Import Random 
    
    word = input("Digite a palavra secreta!: ")
    word = word.upper()
    
    so_far = "-" * len(word) # One dash for each letter in word to be guessed
    
    wrong = 0 # Number of wrong guesses the player has made.
    
    used = [] # An empty list for the letters already guessed.

    print("Bem vindo ao Jogo da Forca! Boa sorte!")

    while wrong < MAX_WRONG and so_far != word:
        print(HANGMAN[wrong])
        print("\nVocê já usou as seguintes letras:\n", used)
        print("\nE até agora, a palavra é:\n", so_far)
    
        guess = input("\nChute uma letra: ")
        guess = guess.upper()
    
        while guess in used:
            print("\nVocê já usou essa letra", guess)
            guess = input("\nChute uma letra: ")
        
        # Add the guess to the list of used letters
        used.append(guess)
    
    # Check if the guess is in the word and then create a new version of
    # so far to include this new letter in all the places where the 
    # letter is in the secret word
        if guess in word:
            print("\nMuito bom!", guess, "está nessa palavra!")
        
        # Create a new so_far to include guess
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                
                else:
                    new += so_far[i]
        
            so_far = new
    
    # If the player's guess isn't in the word, then I let the player know
    # and increase the number of wrong guesses by one.
        else:
            print("\nMe desculpe, mas", guess, "não está nessa palavra.")
            wrong += 1
        
        if wrong == MAX_WRONG:
            print(HANGMAN[wrong])
            print("\nO boneco se enforcou! :(")

    else:
        print("MUITO BOM! VOCÊ VENCEU!")
    
    print("\nA palavra era...", word)
    
def guessthenumber():
    print("\tEsse é um jogo de adivinhação de números!")
    print("\tVocê jogará esse jogo contra mim, o computador!")
    print("\tPense em um número entre 1 e 100 e não se esqueça dele!")
    print("\tEu também vou pensar em um número entre 1 e 100 e você "
        "terá que adivinhar!")
    print("\tPrepare-se!")

    guess = int(input("Tente adivinhar o meu número: "))

    number_human = random.randint(1,100)
    tries_human = 1
    tries_pc = 1
    low = 1
    high = 100

    #print(number_pc)
    while 1:
        if guess > number_human:
            print("É menor que isso...")
    
        elif guess < number_human:
            print("É maior que isso...")
    
        else:
            break
        
        tries_human += 1
        
        print("Agora é a minha vez!")
    
        chute_pc = random.randint(low, high)
    
        print("O seu número secreto é...:", chute_pc,"?")
    
        resposta = str(input(""))
    
        if resposta == "Sim":
            print("UHUL! GANHEI! Eu precisei de", tries_pc, "tentativas!"
            " Foi um jogo difícil, você jogou muito bem!")
            break
    
        elif resposta == "Maior do que isso" or "Maior que isso":
            low = chute_pc - 1
            print("Ok, valeu a tentativa. Agora é sua vez de novo!")
            tries_pc += 1
            guess = int(input("Coloque aqui o seu número: "))

        elif resposta == "Menor do que isso" or "Menor que isso":
            high = chute_pc + 1
            print("Ok, valeu a tentativa. Agora é sua vez de novo!")
            tries_pc += 1
            guess = int(input("Coloque aqui o seu número: "))
        
        elif resposta == "Não":
            print("Ok, valeu a tentativa. Agora é sua vez de novo!")
            tries_pc += 1
            guess = int(input("Coloque aqui o seu número: "))
    
        else:
            print("Eu não entendi o seu input. Pode tentar de novo?")
            guess = int(input("Coloque aqui o seu número: "))
        
        if guess == number_human: 
            print("UHUL! VOCÊ GANHOU! Você precisou de", tries_human, 
                  " tentativas! Foi uma partida disputada, mas você jogou"
                  "muito bem!")
                  
def nomeDeFilho():
    print("Esse é um gerador de nomes de filhos. Digite 4 nomes que você "
    "acha bonitos")

    nm1 = str(input("Coloque aqui o primeiro nome: "))
    nm2 = str(input("Coloque aqui o segundo nome: "))
    nm3 = str(input("Coloque aqui o terceiro nome: "))
    nm4 = str(input("Coloque aqui o quarto nome: "))

    a = len(nm1)
    b = len(nm2)
    c = len(nm3)
    d = len(nm4)

    if a > 4:
        nm1_c = nm1[:4]
   
    else:
       nm1_c = nm1

    if  b > 4:
        nm2_c = nm2[b-4:b]
    
    else:
        nm2_c = nm2[1:b]

    if c > 4:
        nm3_c = nm3[:4]

    else:
        nm3_c = nm3

    if d > 4:
        nm4_c = nm4[d-4:d]

    else:
        nm4_c = nm4[1:d]

    nome_1 = str(nm1_c) + str(nm2_c) 
    nome_2 = str(nm3_c) + str(nm4_c)
    nome_final = nome_1 + " " + nome_2

    print("O nome do seu/sua filho/filha é:", nome_final)
    
    main()

# PROGRAMA PRINCIPAL

x = main()
while x != 5:
    if x == 1:
        maze()
        x = main()
    elif x == 2:
        forca()
        x = main()
    elif x == 3:
        guessthenumber()
        x = main()
    elif x == 4:
        nomeDeFilho()
        x = main()