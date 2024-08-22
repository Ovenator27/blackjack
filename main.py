import random 
from art import logo
from os import system


def deal_card():
    """Returns a random card from the deck"""
    cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    return random.choice(cards)

def calculate_score(hand):
    """Takes a list of cards and calculates the total value of the cards"""
    hand_values = []

    # Translates card faces into int values
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            hand_values.append(10)
        elif card == 'A':
            hand_values.append(11)
        else:
            hand_values.append(int(card))
            
    total = sum(hand_values)
    
    # Checks for Blackjack, returns 0 if true
    if total == 21 and len(hand_values) == 2:
        return 0

    # Checks for high aces causing bust and changes to low aces
    if total > 21 and 11 in hand_values:
        while total > 21 and 11 in hand_values:
            hand_values.remove(11)
            hand_values.append(1)
            total = sum(hand_values)
            
    return total

def compare(player_hand, player_score, computer_hand, computer_score):
    """Compares scores and prints the winner to the console with final scores"""
    print()
    
    if player_score == computer_score:
        print("It's a draw")
        
    elif player_score == 0:
        print("You got Blackjack, you win!")
        player_score = 21
        
    elif computer_score == 0:
        print("Dealer has Blackjack, you lose")
        computer_score = 21
        
    elif player_score > 21:
        print("Bust! You lose")
        
    elif computer_score > 21:
        print("Dealer busts, you win!")
        
    elif computer_score > player_score:
        print("You lose")
        
    else:
        print("You win!")
        
    print()
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand {computer_hand}, final score: {computer_score}")
    print()

def restart():
    """Allows restarting of game"""
    play_again = input("Would you like to play again? type 'y' to restart or any other key to finish: ").lower()
    
    if play_again == 'y':
        play_game()
        
def play_game():   
    game_over = False
    player_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]
    
    system('clear')
    print(logo)
    while not game_over:
        player_score = calculate_score(player_hand)
        computer_score = calculate_score(computer_hand)
    
        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
            compare(player_hand, player_score, computer_hand, computer_score)
            
        else:
            print(f"\nYour hand: {player_hand}, current score: {player_score}")
            print(f"Dealer's first card: '{computer_hand[0]}'\n")
            player_choice = input("Would you like another card? Type 'y' for another card or 'n' to pass to the dealer: ").lower()
            if player_choice == 'y':
                player_hand.append(deal_card())
                
            elif player_choice != 'n':
                print("\nInvalid choice")
                
            else:
                game_over = True
                while computer_score < 17 and computer_score != 0:
                    computer_hand.append(deal_card())
                    computer_score = calculate_score(computer_hand)
                    
                compare(player_hand, player_score, computer_hand, computer_score)
                    
    restart()      
    
print(logo)
if input("Welcome, would you like to play Blackjack? Type 'y' to start: ").lower() == 'y':
    play_game()