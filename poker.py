"""poker module which is built to find out the winner when only 2 player are playing with one deck of cards"""
import random
from collections import Counter


#setting up some initial variables
values = ['2','3','4','5','6','7','8','9','jack','queen','king','ace']
suits = ['spades','clubs','hearts','diamonds']
values_dict={'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'jack':10,'queen':11,'king':12,'ace':13}


#Function to create a deck using a list comprehensions
def create_deck_list_comprehension():
    """ This function creates a deck using list comprehensions"""
    deck = [(i,j) for i in values for j in suits]
    return deck #returns a list

def create_deck():
    """ This function creates a deck without using list comprehensions"""
    deck = []
    for i in values:
        for j in suits:
            deck.append((i,j)) #appends the deck list with a tuple of value and suit

    return deck #returns a list


def transform_cards(card:'tuple')->"tuple" :
    """ This function changes the type of value from string to int
    INPUT: 
        this function takes a card(type-tuple of value,suit)
    OUTPUT: 
        this function returns a tuple of value,suit
    """
    value,suit=card #unpacking the iterables
    if value not in values or suit not in suits: #checking for invalid values and suits
        raise ValueError("Inappropriate card: Please enter appropriate card values!!!")
    else:
        value = values_dict[value] #getting the int(value) using dict
        return value,suit #returns a tuple



def check_suits(lists:'list')->'bool':
    """ This function checks if the cards are of the same suit
    INPUT: 
        this function takes a list
    OUTPUT: 
        this function returns a bool value
    """
    return lists.count(lists[0]) == len(lists) #checks if all the elements of the inputed suits list are the same



def check_sequence(lists:'list')->'bool':
    """ This function checks if the cards are in a sequence
    INPUT: 
        this function takes a list
    OUTPUT:
        this function returns a bool value
    """
    return sorted(lists) == list(range(min(lists),max(lists)+1)) #checks if the elements are in a sequence


def kind_counter(lists:'list')->'tuple':
    """ This function counts the kind of each card in the list
    INPUT:
        this function takes a list
    OUTPUT:
        returns a tuple of
            result: int :gives the maximum value with maximum count
            val: int : gives the count of result
            no_pairs: int : number of pairs in the lists
            full_house: bool : returns True if its a full-house
    """
    a = Counter(lists) #gets a dictionary of values
    val = max(a.values()) #finds the value which has max count
    key_find = []
    full_house = False #starting with a falsy condition
    for key,value in a.items(): #gets a list of values with max count
        if value == val:
            key_find.append(key)
    result = max(key_find)
    no_pairs = len(key_find) if val >1 else 0
    if len(lists) == 5 and len(a) == 2: #checks for a full-house
        full_house = True

    return result, val , no_pairs , full_house #returns a tuple



def cards_evaluation(cards:'list')->'tuple':
    """ This function evaluates the cards of the players
    INPUT:
        takes a list of cards of one player
    OUTPUT:
        gives a tuple of 
            order : int : gives the ranking of the player cards based on standard poker rules
            result : int : maximum value of card of the player
    """
    player_suit = []
    player_values = []
    for i,j in cards: #creates lists of suits and values
        player_suit.append(j)
        player_values.append(i)
    sequence = check_sequence(player_values) #checks if cards are in sequence
    kind = check_suits(player_suit) #checks if cards are of same suit
    #following statements are based on poker rules 
    if kind:
        if sequence:
            result = max(player_values)
            order = 2 if result  < 13 else 1 #checks rule number 1:Royal Flush and 2: Straight Flush
        else:
            order = 5 #checks rule number 5:Flush
            result = max(player_values)       
    elif sequence:
        order = 6 #checks rule number 6:Straight
        result = max(player_values)
    else:
        result,count_of_result,no_pairs,full_house = kind_counter(player_values)
        if count_of_result == 4:
            order = 3 #checks rule number 3:Four of a kind
        elif count_of_result == 3 and full_house == True:
            order = 4 #checks rule number 4: Full house
        elif count_of_result == 3:
            order = 7 #checks rule number 7: Three of a kind
        elif count_of_result == 2 and no_pairs == 2:
            order = 8 #checks rule number 8: Two pair
        elif count_of_result == 2 and no_pairs == 1:
            order = 9 #checks rule number 9:One pair
        else:
            order = 10 #checks rule number 10: High card   


    return order,result #returns a tuple



def winner(player1:'list', player2:'list')->'str':
    """ This function returns the winner of the game
    INPUT:
        takes two list of cards of players
    OUTPUT:
        returns the result/winner player
    """

    order1,result1 = cards_evaluation(player1) #evaluates player1 cards
    order2,result2 = cards_evaluation(player2) # evaluates player2 cards
    if order1 == order2:
        if result1 == result2: #checks for a draw
            return 'draw'
        else: #checks for a player with highest value when of same order
            return 'player1' if result1 > result2 else 'player2'
    else: #checks for player with lowest order
        return 'player1' if order1<order2 else 'player2'




def poker(suits:'list' = suits, values:'list' = values, number_of_players:'int' = 2)->'tuple':
    """ This function plays the game poker with 2 players and one deck
    INPUT:
        suits: list : list of all the suits : default = suits
        values: list : list of all the values : default = values
        number_of_players: int : number of players : default = 2
    OUTPUT:
        returns a tuple
        player1: list of cards of player1
        player2: list of card of player2
        string: the result/winner of the game
    """
    deck = create_deck_list_comprehension() #creates a deck

    player1 = []
    player2 = []

    x = random.choice([3,4,5]) #chooses randomly the number of cards each player can have in the game

    for card in range(x):
        random.shuffle(deck) #shuffles the deck
        player1.append(transform_cards(deck.pop())) #distributes a card to player1
        player2.append(transform_cards(deck.pop())) #distributes a card to player2

    return player1,player2, winner(player1,player2) #returns a tuple

