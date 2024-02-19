import random
from art import logo
from replit import clear

def deal():
    #cards = {"Ace": 11 , 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':10, 'Q':10, 'K':10}
    cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10,10,10]
    card = random.choice(cards_list)
    return card

def calculate_sum(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user, computer):
    if user == computer:
        print("It's a Draw")
    elif computer == 0:
        print("It's Bot's Blackjack.. You lost")
    elif user == 0:
        print("It's a Blackjack.. You Win")
    elif user>21:
        print("Score more than 21... Lose")
    elif computer>21:
        print("Bot's score more than 21.. Win")
    elif user>computer:
        print("Your Score more than Bot.. Win")
    else:
        print("Bot's Score more than You... Losst")


def play():
    print(logo)
#ask = input("Do you want to play: ").lower()
#if ask == 'y' or ask == 'yes':
    user_cards = []
    computer_cards = []
    end = False

    for i in range(2):
        user_cards.append(deal())
        computer_cards.append(deal())

    while not end:
        user_score = calculate_sum(user_cards)
        computer_score = calculate_sum(computer_cards)
        print(f"Your Cards: {user_cards}, Current Score: {user_score}")
        print(f"Computer First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
          end = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal())
                user_score = calculate_sum(user_cards)
            else:
                end = True

        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal())
            computer_score = calculate_sum(computer_cards)

    print(f"   Your final cards: {user_cards}, final score: {user_score}")
    print(f"   Computer's final cards: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

end_again = False
while end_again == False:
    inn = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") 
    if inn == 'y' or inn == 'yes':
        clear()
        play()
        end_again = False
        
    else:
        print("Good Bye!")
        end_again = True
    