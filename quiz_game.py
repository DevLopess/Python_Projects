print("Bem vido ao meu quiz!")

playing = input("Queres jogar?(S ou N): ")

if playing.lower() != "s":
    quit()

score = 0


print("Muito bem vamos começar o jogo então")

answer = input("O que significa CPU?\n1.teste1\n2.teste2\n3.central processing unit\n4.tetetet ")

if answer.lower() == "3":
    print("Certo!")

else:
    print("Errado")