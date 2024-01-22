# Spin the wheel game

import random
import sys


def print_intro_text():
    print('=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=')
    print('         Welcome to spin the wheel')
    print('                  With bets')
    print('=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=')
    print('There is 5 options on the wheel:')
    print('Green doubles your money')
    print('Blue loses your money')
    print('Yellow 1.5x your money')
    print('Red returns your money')
    print('Orange loses your money')


def get_deposit(old_balance=0):
    while True:
        deposit = input('Please deposit money to play: £')
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                new_balance = old_balance + deposit
                print('Thank you your balance is currently: £', new_balance)
                return new_balance
            print('Please deposit at least £1.')
        else:
            print('Please enter a numerical amount.')


def get_bet(balance):
    while True:
        bet = input('Please enter how much you\'d like to bet on this spin: £')
        if bet.isdigit():
            bet = int(bet)
            if bet <= balance:
                print('Thank you, you have just bet: £', bet)
                return bet
            print('Please bet an amount that is no larger than your balance of: £', balance)
        else:
            print('Please enter a numerical amount or a an amount above 0.')


def play(balance):
    while True:
        bet = get_bet(balance)
        balance -= bet

        # The rest of this code is left as an exercise to improve / refactor.

        colour = 'green'
        spin = random.randint(1, 5)
        if spin == 1:
            outcome = bet * 2
        elif spin == 2:
            outcome = bet - bet
            colour = 'Blue'
        elif spin == 3:
            outcome = bet * 1.5
            colour = 'Yellow'
        elif spin == 4:
            outcome = bet
            colour = 'Red'
        else:
            outcome = bet - bet  # FIXME
            colour = 'Orange'
        start = input('Hit enter to spin the wheel')
        while start != '':
            sys.exit()
        print('It landed on:', colour)
        if outcome == 0:
            print('That means you lost your bet of £', bet)
        if outcome == bet:
            print('You got your money back.')
        if outcome > bet:
            print('You made: £', outcome - bet, 'So got £', outcome, 'back.')
        print('Your balance is now: £', balance + outcome)
        balance = balance+outcome
        again = input('Would you like to play another round? ').lower()
        if again in ['yes', 'y']:
            if balance < 1:
                money = False
                while not money:
                    deposit = input('You have run out of money. Please deposit more money to keep playing. £')
                    if deposit.isdigit():
                        deposit = int(deposit)
                        if deposit > 0:
                            print('Thank you your balance is currently: £', balance + deposit)
                            balance = deposit + balance
                            money = True
                        else:
                            print('Please deposit at least £1.')
                    else:
                        print('Please enter a numerical amount.')
        else:
            print('Thank you for playing')
            print('Your final balance was: £', balance)
            if balance > 0:
                withdraw = input('Would you like to withdraw your money? ').lower()
                if withdraw in ['yes', 'y', 'please']:
                    print('We have deposited your balance of £', balance, 'into your bank account.')
                    balance = balance - balance
                    print('Your balance is now: £', balance)
                else:
                    print('That\'s ok, we will keep your money for next time you play.')
            break


def main():
    print_intro_text()
    balance = get_deposit()
    play(balance)


if __name__ == '__main__':
    main()