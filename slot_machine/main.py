import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

balance = 0

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet

    return winnings

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range (cols):
        column = []
        copy_all_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(copy_all_symbols)
            copy_all_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input("Banca inicial?: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("Insira um valora maior que zero")
                continue
        else:
            print("Insira um valor válido")
            continue

    return amount

def get_number_of_lines():
    while True:
        amount = input("Em quantas linhas quer apostar?(MAXIMO de " + str(MAX_LINES) +" LINHAS):")
        if amount.isdigit():
            amount = int(amount)
            if amount >= 1 and amount <= MAX_LINES:
                break
            else:
                print("Insira um valor entre 1 e " + str(MAX_LINES) + "")
                continue
        else:
            print("Insira um valor válido")
            continue

    return amount

def get_bet():
    while True:
        bet = input("Quanto quer apostar por cada linha: ")
        if bet.isdigit():
            bet = int(bet)
            if MAX_BET >= bet >= MIN_BET:
                break
            else:
                print(f"Minimo de aposta = {MIN_BET}$ ||| Maximos de aposta = {MAX_BET}$")
                continue
        else:
            print("Insira um valor válido")
            continue
    return bet

def spin(balance):
    lines = get_number_of_lines()
    print(balance, lines)
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Banca Insuficiente, banca atual: {balance} $")
            continue
        else:
            break

    print(f"Aposta de {bet}$ em {lines} linhas. Aposta total de : {bet*lines}$")

    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)

    winnings = check_winnings(slots,lines,bet,symbol_values)
    print(f"Ganhou: {winnings}.")
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Banca Atual:{balance}")
        spin_ = input("Press enter to play (q to quit)")
        if spin_ == "q":
            break
        balance += spin(balance)
    print(f"Saiu com:{balance}")

main()

