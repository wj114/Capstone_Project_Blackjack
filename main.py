from art import logo
import random
from os import system


def clear():
    system('clear')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card_to_deal = random.choice(cards)
    return card_to_deal


def calculate_score(card):
    """Take list of cards and return the total points of cards"""

    # checking is it blackjack
    if len(card) == 2 and sum(card) == 21:
        return 0

    points = 0

    if "11" in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    for i in card:
        points += i
    return points


def compare(user_score, computer_score):
    """To compare the points """
    if user_score == computer_score:
        return "It's a draw."
    elif user_score == 0:
        return "You have BLACKJACK! You WIN! :)"
    elif computer_score == 0:
        return "Computer has BLACKJACK! You lose :("
    elif user_score < 21 and computer_score > 21:
        return "Computer went over, you win!! :)"
    elif user_score > 21 and computer_score < 21:
        return "You went over, you lose! :("
    elif user_score > computer_score:
        return " You have bigger points, you win! :)"
    elif user_score < computer_score:
        return "You have smaller points, you lose! :("


def blackjack():
    """This is the main game function"""
    game_over = False

    player = []
    computer = []

    for _ in range(2):
        player.append(deal_card())
        computer.append(deal_card())

    while not game_over:
        player_points = calculate_score(player)
        computer_points = calculate_score(computer)

        # check
        print(f"You cards: {player}, your points: {player_points}")
        print(f"Computer's first cards: {computer[0]}, * ")

        if player_points == 0 or computer_points == 0 or player_points > 21:
            game_over = True
        else:
            ongoing = input("Do you want to draw another card? Type 'y' to continue and 'n' to not draw.\n")

            if ongoing == "y":
                player.append(deal_card())
                player_points = calculate_score(player)

            elif ongoing == "n":
                game_over = True

    while computer_points != 0 and computer_points < 16:
        computer.append(deal_card())
        computer_points = calculate_score(computer)

    print(f"You cards: {player}, your points: {player_points}")
    print(f"Computer's cards: {computer}, computer points: {computer_points}")
    print(compare(player_points, computer_points))


# Starting the code by asking user whether they want to play
while input("Do you want to play BLACKJACK? Type 'y' for yes and 'n' for no.\n") == 'y':
    clear()
    print(logo)

    print("@@@****** Welcome to Blackjack ******@@@")
    blackjack()
