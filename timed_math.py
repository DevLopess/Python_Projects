import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " +  operator + " " + str(right)

    answer = eval(expr)


    return expr, answer

start_time = time.time()


for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()

    print("Problem #" + str(i+1) + ":" + expr)
    while True:
        guess = input(":")
        if guess == str(answer):
            print("CERTO")
            break
        else:
            print("ERROU!")

end_time = time.time()

total_time = round(end_time - start_time)

print("Terminas-te em", total_time , "!!!!")