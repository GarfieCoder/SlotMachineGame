import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS= 3

symbol_count = {
    'A': 2,
    'B': 4,
    'C': 6,
    'D': 8
}

def get_slot_score(columns, lines, bet, values):
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
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for row in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    rows = len(columns[0])
    for row in range(rows):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Enter the amount to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print('Amount must be greater than 0.')
        else:
            print('Please enter a number.')
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid number of lines.')
        else:
            print('Please enter a number.')
    return lines


def get_bet():
    while True:
        bet = input("Enter the amount you would like to bet: $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Amount must be between ${MIN_BET} and ${MAX_BET}.')
        else:
            print('Please enter a number.')
    return bet



def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print("You do not have enough balance to place this bet.")
        else:
            break


    print("You have deposited: $", balance)
    print("You have chosen to bet on", lines, "lines.")
    
    print(f'You are betting ${bet}, on each line. Your total bet is ${total_bet}.')

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings = get_slot_score(slots,lines,bet, symbol_count)
    print(f'You won ${winnings}.')


main()
