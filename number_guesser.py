import random

num_max = input("Qual é o número máximo?: ")

if num_max.isdigit():
    num_max = int(num_max)
    if num_max <= 0:
        print("É necessário um número maior que 0!")
        quit()

else:
    print("É necessario um número!")

random_number = random.randrange(0,num_max)
print(random_number)

choosen_number = input("Escolhe um número dentro do range escolhido:")

while random_number != int(choosen_number) :
    if(int(choosen_number)<random_number):
        print("O teu número está abaixo da resposta!")
    else:
        print("o teu número está acima da resposta")
    choosen_number = input("Escolhe um número dentro do range escolhido:")


print("Acertaste!!!")

