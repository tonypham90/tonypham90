############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.


from art import logo
from blackjact_card import card
import os
print(logo)
# print (card)
card = {
'A': 11,  # value of the ace is high until it needs to be low
'2': 2,
'3': 3,
'4': 4,
'5': 5,
'6': 6,
'7': 7,
'8': 8,
'9': 9,
'10': 10,
'J': 10,
'Q': 10,
'K': 10    
}
suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
suits_symbols = ['♠', '♦', '♥', '♣']
# print(suits_symbols[1])
#Clean screen:
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
playcard=[]
def add_card(rank,value,playcard):
    faces = ["Diamons","Clubs","Spades","Hearts"]
    suits_symbols = ['♠', '♦', '♥', '♣']
    card = {}
    index=0
    while index < 4:
        # print (card)
        card['rank'] = rank
        # print (card)
        card['face'] = faces[index]
        # print(card) 
        card['value'] = value
        # print(card)
        card["symbol"] = suits_symbols[index]
        playcard.append(dict(card))
        index += 1  
    return playcard

# Create playcard:
for rank in card:
    Value_card = card[rank]
    add_card(rank,Value_card,playcard)
stock_playcard=playcard
# print(playcard)
# print(len(playcard))
# # # gaming
# # Add user:
def add_user():
    user={}
    user['name']=input("Player Name: ")
    user['money']=float(input('How much money do you wanna have to play? $'))
    user_name=user['name']
    user_balance = user['money'] 
    print(f'Welcome {user_name} to blackjack game with your bank is {user_balance}$')
    return user

Player=add_user()

# definition function take card and refresh stock card after take card.
import random
def take_card(stock_playcard): #take new card
    export_card=random.sample(stock_playcard,1)
    return export_card
def renew_stockcard(stock_playcard,card_remove): #remove card
    stock_playcard.remove(card_remove[0])
    return stock_playcard
def take_card_reset(stock_playcard): # one turn take card
    result = {}
    card = take_card(stock_playcard)
    stock = renew_stockcard(stock_playcard,card)
    result["Card"] = card
    result["stock_card"] = stock
    return result

# Total value of card:
def total_value(member_card):
    card_no=len(member_card)
    value = 0
    for card in member_card:
        card_rank = card ["rank"]
        #check card rank is A and number of card is higher than 2, value will be 1,
        if card_no > 2 and card_rank == "A":
            card_value = 1
        else:
            card_value = card['value']
        value = card_value + value
    return value


            


# Print card
def print_card(member_card):
    for card in member_card:
        card_rank = card["rank"]
        card_symbol = card["symbol"]
        print(f'Card: {card_rank}{card_symbol}\n')
    value=total_value(member_card)
    print(f'\nTotal your card value is {value}')

def print_com_card(com_card,hiden):
    if hiden:
        com_2nd_rank = com_card [1]["rank"]
        com_2nd_symbol = com_card [1]["symbol"]
        print(f'the first card is hiden\n and The 2nd card of Computer is {com_2nd_rank}{com_2nd_symbol}')
    else:
        for card in com_card:
            card_rank = card["rank"]
            card_symbol = card["symbol"]
            print(f'Card: {card_rank}{card_symbol}\n')
        value=total_value(com_card)
        print(f'\nTotal com card value is {value}')

def winner(playcard,comcard,money_deal,double):
    # cls()
    print("\nCom card is\n")
    print_card(comcard)
    print("\nyour card is\n")
    print_card(playcard)
    print('You win')
    money_earn = money_deal*2
    if double:
        money_earn += money_deal
    print(f'you earn {money_earn}')
    return money_earn
def loser(playcard,comcard,money_deal,double):
    # cls()
    print("Com card is\n")
    print_card(comcard)

    print("\nyour card is\n")
    print_card(playcard)
    print('You loses')
    money_earn = 0
    if double:
        money_earn -= money_deal
    return money_earn
def draw(playcard,comcard,money_deal):
    # cls()
    print("Com card is")
    print_card(comcard)
    print("your card is")
    print_card(playcard)
    print('Draw')
    money_earn = money_deal
    print(f'you earn {money_earn}')
    return money_earn

# Check winner and money player can earn:
def money_game(playcard,comcard,money_deal,double):
    print_com_card(comcard,False)
    player_card_value=total_value(playcard)
    com_card_value = total_value (comcard)
    if len(playcard) == 2 and player_card_value ==21:
        if player_card_value > com_card_value:
            money_earn=winner(playcard,comcard,money_deal,double)
        elif player_card_value == com_card_value:
            money_earn = draw(playcard,comcard,money_deal)
        else:
            money_earn = loser(playcard,comcard,money_deal,double)
    elif len(playcard) == 5 and player_card_value <=21:
        if len(comcard) <5:
           money_earn=winner(playcard,comcard,money_deal,double)
        elif len(comcard) ==5:
            if player_card_value < com_card_value:
                money_earn = loser(playcard,comcard,money_deal,double)
            elif player_card_value == com_card_value:
                money_earn = draw(playcard,comcard,money_deal)
            else:
                money_earn=winner(playcard,comcard,money_deal,double)
    elif len(comcard)==2 and com_card_value <= 21 and len(playcard) < 5:
        money_earn = loser(playcard,comcard,money_deal,double)
    elif (player_card_value <= 21 and player_card_value>=15) and (com_card_value <= 21 and com_card_value>=15):
        if player_card_value > com_card_value:
            money_earn=winner(playcard,comcard,money_deal,double)
        elif player_card_value == com_card_value:
            money_earn = draw(playcard,comcard,money_deal)
        else:
            money_earn = loser(playcard,comcard,money_deal,double)
    elif player_card_value > 21:
        if com_card_value > 21:
            money_earn = draw(playcard,comcard,money_deal)
        else:
            money_earn = loser(playcard,comcard,money_deal,double)
    return money_earn

# Game flow per match
def game_flow(deal_money,stock_card,double):
    player_card=[]
    play_card_value = 0
    computer_card=[]
    com_card_value = 0
    stock_card_play=stock_card

# Com take full card
    while len(computer_card) < 6 and com_card_value < 17:
        take_turn = take_card_reset(stock_card_play)
        stock_card_play = take_turn["stock_card"]
        Card = take_turn["Card"][0]
        computer_card.append(Card)
        com_card_value = total_value(computer_card)
        if len(computer_card) == 2:
            print_com_card(computer_card,True)
            computer_2card = computer_card
            # com_2card_value = total_value(computer_2card)


# Player take 2 first card:
    while len(player_card) < 2:
        take_turn = take_card_reset(stock_card_play)
        stock_card_play = take_turn["stock_card"]
        Card = take_turn["Card"][0]
        player_card.append(Card)
        play_card_value = total_value(player_card)
    print("your card:")
    print_card(player_card)
    if play_card_value == 21:# when Ace, and Com no Ace, win no conditions
        money_earn=money_game(player_card,computer_2card,deal_money,double)
        return money_earn


    # continue take card:
    while len(player_card) < 6:
        if double == True and len(player_card) == 2:
            double_deal = input(f'Do you wanna double money? (y/n)')
            if double_deal == "y":
                take_turn = take_card_reset(stock_card_play)
                stock_card_play = take_turn["stock_card"]
                Card = take_turn["Card"][0]
                player_card.append(Card)
                play_card_value = total_value(player_card)
                money_earn=money_game(player_card,computer_card,deal_money,double)
                return money_earn
            else:
                double == False
                mem_take_card = input(f'Do you wanna take another card? (y/n)')
                if mem_take_card != "y":
                    money_earn=money_game(player_card,computer_card,deal_money,double)
                    return money_earn
                else:
                    take_turn = take_card_reset(stock_card_play)
                    stock_card_play = take_turn["stock_card"]
                    Card = take_turn["Card"][0]
                    player_card.append(Card)
                    play_card_value = total_value(player_card)
                
                print("Com card:")
                print_com_card(computer_card,True)
                money_earn=money_game(player_card,computer_card,deal_money,double)
                return money_earn
        else:
            mem_take_card = input(f'Do you wanna take another card? (y/n)')
            if mem_take_card != "y":
                money_earn=money_game(player_card,computer_card,deal_money,double)
                return money_earn
            else:
                take_turn = take_card_reset(stock_card_play)
                stock_card_play = take_turn["stock_card"]
                Card = take_turn["Card"][0]
                player_card.append(Card)
                play_card_value = total_value(player_card)
                print_card(player_card)
                print("Com card:")
                print_com_card(computer_card,True)

            # cls()
            money_earn=money_game(player_card,computer_card,deal_money,double)
            return money_earn

def game_on(player,stock_playcard):
    play = True
    rounds = int(input(f'How many game do you wanna play? '))
    banks = player ['money']
    player_name = player ['name']
    games = 0
    while games <= rounds and banks > 0:
        games += 1
        print(f'\n\n\n------------------\nRounds {games}')
        deal_money = float(input(f'Money deal: $'))
        banks -= deal_money
        if banks/deal_money >= 2:
            double = True
        else:
            double = False
        money_earn = game_flow(deal_money,stock_playcard,double)
        banks += money_earn
        print(f'Balance of {player_name} is {banks}$')
        if banks == 0:
            print( "Game over")
    game = input(f'Do you want to play again? (y/n)')
    if game == "y":
        play = True
    else:
        play = False
    return play

play = True
while play is True:
    play = game_on(Player,stock_playcard)
    

    
        
    


