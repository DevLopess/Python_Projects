import random
import time

bot_wins = 0
player_wins = 0

print("Bem vindo ao jogo PEDRA PAPEL OU TESOURA")

print("Para jogar insere R(PEDRA) P(PAPEL) ou T(TESOURA), para terminar o jogo basta escrever \" sair\"")

in_start = input("Podemos dar inicio ao jogo?(SIM OU NAO): ")

if in_start.lower() != "sim":
    quit()

play=""

options = ["r","p","s"]

while play.lower() != "sair":
    bot_choice = options[random.randrange(0,3)] #escolha do computador (pedra:0,papel:1,tesoura:2)
    print("PEDRA")
    time.sleep(0.5)
    print("PAPEL")
    time.sleep(0.5)
    print("OU")
    time.sleep(0.5)
    print("TESOURA!!!")
    play = input(":").lower()
    if play not in options:  #verificacao
        continue
    if play == "r" and bot_choice == "s":
        print("Ganhaste")
        player_wins += 1
    elif play == "p" and bot_choice == "r":
        print("Ganhaste")
        player_wins += 1
    elif play == "s" and bot_choice == "p":
        print("Ganhaste")
        player_wins += 1
    else:
        print("Perdeste :/")
        bot_wins += 1

print("Ganhaste ",player_wins ," vezes")

print("Perdeste ",bot_wins ," vezes")
