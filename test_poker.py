import pytest
import os
import inspect
import re
import poker
import test_poker

README_CONTENT_CHECK_FOR=['poker','comprehensions','deck','sequence','suits','players','spades']


#-----------------General tests----------------------------------

def test_session6_readme_exists():
    """ Checks if README file exists"""
    assert os.path.isfile("README.md"), "README.md file missing!"
    
def test_session6_readme_500_words():
    """ Checks if README file has a minimum of 500 words"""
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session6_readme_proper_description():
    """ Checks if README file has description of all the functions/classes."""
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/classes well in your README.md file"
    
def test_session6_readme_file_for_more_than_10_hashes():
    """Checks if README file has proper formatting (minimum of 10 hashes)"""
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10
    
    
def test_session6_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
    """
    lines = inspect.getsource(poker)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"
        
        
def test_session6_function_name_had_cap_letter():
    """ test fails if Capital letter(s) used for function names """
    functions = inspect.getmembers(poker, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
        
        
def test_function_count():
    """ tests number of test function > 20 in test_poker file"""
    functions =inspect.getmembers(test_poker, inspect.isfunction)
    assert len(functions) > 20, 'Test cases seems to be low. Work harder man...'
    
    
def test_function_repeatations():
    """ tests if any repeated tests in test_poker file"""
    functions = inspect.getmembers(test_poker, inspect.isfunction)
    names = []
    for function in functions:
        names.append(function)
    assert len(names) == len(set(names)), 'Test cases seems to be repeating...'
        
        
        
        
#------------------------create deck---------------------------------

deck = [('2', 'spades'), ('2', 'clubs'), ('2', 'hearts'), ('2', 'diamonds'), ('3', 'spades'), ('3', 'clubs'), ('3', 'hearts'), ('3', 'diamonds'), ('4', 'spades'), ('4', 'clubs'), ('4', 'hearts'), ('4', 'diamonds'), ('5', 'spades'), ('5', 'clubs'), ('5', 'hearts'), ('5', 'diamonds'), ('6', 'spades'), ('6', 'clubs'), ('6', 'hearts'), ('6', 'diamonds'), ('7', 'spades'), ('7', 'clubs'), ('7', 'hearts'), ('7', 'diamonds'), ('8', 'spades'), ('8', 'clubs'), ('8', 'hearts'), ('8', 'diamonds'), ('9', 'spades'), ('9', 'clubs'), ('9', 'hearts'), ('9', 'diamonds'), ('jack', 'spades'), ('jack', 'clubs'), ('jack', 'hearts'), ('jack', 'diamonds'), ('queen', 'spades'), ('queen', 'clubs'), ('queen', 'hearts'), ('queen', 'diamonds'), ('king', 'spades'), ('king', 'clubs'), ('king', 'hearts'), ('king', 'diamonds'), ('ace', 'spades'), ('ace', 'clubs'), ('ace', 'hearts'), ('ace', 'diamonds')]

def test_check_create_deck_list_comprehension():
    """ This test checks the deck created using create_deck_list_comprehension function"""
    assert poker.create_deck_list_comprehension() == deck , "Creating deck with list comprehension is not working"
    
def test_check_create_deck():
    """ This test checks the deck created using create_deck function"""
    assert poker.create_deck() == deck , "Creating deck with normal function is not working"
    
#----------------------- checking transform cards-----------------

cards = [('3','spades'),('9','clubs'),('ace','diamonds'),('jack', 'diamonds'),('king', 'hearts'),('queen', 'clubs')]
results = [(3, 'spades'),(9, 'clubs'),(13, 'diamonds'),(10, 'diamonds'),(12, 'hearts'),(11, 'clubs')]

def test_check_transform_cards_with_no_arguments():
    """ This test checks transform_cards with no arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'card'*"):
        poker.transform_cards()
        
        
def test_check_transform_cards():
    """ This test checks transform_cards with proper arguments"""
    for i in range(len(cards)):
        assert poker.transform_cards(cards[i]) == results[i],'Transform cards function did not work as intended'
        
        
        
def test_check_transform_cards_for_inappropriate_cards():
    """ This test checks transform_cards with improper arguments"""
    with pytest.raises(ValueError, match=r".*Inappropriate card*"):
         poker.transform_cards(('Minister','spades'))
         
         
         
#------------------------tests check_sequence ------------------------
lists = [[2,7,9,4,3,5,8,6],[3,6,1,4]]

def test_check_sequence_with_no_arguments():
    """ This test checks check_sequence with no arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'lists'*"):
        poker.check_sequence()
def test_check_sequence_for_a_sequence():
    """ This test checks check_sequence with proper sequential arguments"""
    assert poker.check_sequence(lists[0]) == True, "Check sequence is not working!!!!!!"

def test_check_sequence_for_not_a_sequence():
    """ This test checks check_sequence with non-sequential arguments"""
    assert poker.check_sequence(lists[1]) == False, "Check sequence is not working!!!!!!"
    
    
#---------------------------tests check_suits-----------
suits = [['spades','clubs','hearts','clubs'],['diamonds','diamonds','diamonds']]

def test_check_suits_with_no_arguments():
    """ This test checks check_suits with no arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'lists'*"):
        poker.check_suits()
        
def test_check_suits_for_different_suits():
    """ This test checks check_suits with list of different suits"""
    assert poker.check_suits(suits[0])==False,"Check suits is not working!!!!!!!"


def test_check_suits_for_same_suits():
    """ This test checks check_suits with list of same suits"""
    assert poker.check_suits(suits[1])==True,"Check suits is not working!!!!!!!"
    
    
#---------------------------tests kind_counter---------------
lits = [[2,5,1,3,2],[2,5,5,2,2],[4,7,9],[10,3,7]]


def test_kind_counter():
    """ This test verifies the value of kind_counter function"""
    assert poker.kind_counter(lits[0]) == (2,2,1,False) ,"Kind Counter not working!!!!!"
    assert poker.kind_counter(lits[1]) == (2,3,1,True) ,"Kind Counter not working!!!!!"
    assert poker.kind_counter(lits[2]) == (9,1,0,False) ,"Kind Counter not working!!!!!"
    assert poker.kind_counter(lits[3]) ==  (10,1,0,False),"Kind Counter not working!!!!!"
    
    
    
#-------------------tests cards_evaluation----------------

list_of_players_cards=[[(3, 'hearts'), (8, 'hearts'), (11, 'hearts'), (6, 'hearts')],[(7, 'diamonds'), (9, 'diamonds'), (12, 'diamonds'), (5, 'clubs')],[(2, 'diamonds'), (9, 'spades'), (5, 'hearts'), (6, 'diamonds')]]

def test_cards_evaluation():
    """ This test verifies the value of cards_evaluation function"""
    assert poker.cards_evaluation(list_of_players_cards[0]) == (5,11),"Cards are not evaluated properly!!!!!"
    assert poker.cards_evaluation(list_of_players_cards[1]) == (10,12),"Cards are not evaluated properly!!!!!"
    assert poker.cards_evaluation(list_of_players_cards[2]) == (10,9),"Cards are not evaluated properly!!!!!"
    
    
    
#-----------------tests winner------------------



play1 = [[(4, 'clubs'), (7, 'spades'), (9, 'diamonds'), (2, 'spades'), (6, 'clubs')],[(13, 'hearts'), (8, 'hearts'), (4, 'spades'), (13, 'spades'), (11, 'hearts')]]
play2 = [[(9, 'hearts'), (5, 'clubs'), (8, 'spades'), (4, 'diamonds'), (5, 'diamonds')],[(10, 'hearts'), (3, 'hearts'), (9, 'clubs'), (4, 'spades'), (12, 'spades')]]
play3 = [[(10, 'spades'), (12, 'hearts'), (9, 'hearts'), (4, 'hearts')],[(8, 'spades'), (6, 'spades'), (9, 'diamonds'), (7, 'spades')]]
play4 = [[(4, 'diamonds'), (3, 'spades'), (8, 'hearts'), (13, 'clubs'), (11, 'spades')], [(8, 'diamonds'), (6, 'clubs'), (5, 'clubs'), (3, 'clubs'), (9, 'hearts')]]
play5 = [[(7, 'clubs'), (11, 'clubs'), (4, 'spades'), (12, 'spades')], [(3, 'diamonds'), (10, 'spades'), (7, 'spades'), (9, 'clubs')]]
play6 = [[(12, 'clubs'), (5, 'hearts'), (7, 'hearts'), (6, 'spades'), (4, 'diamonds')], [(13, 'spades'), (13, 'hearts'), (4, 'clubs'), (3, 'diamonds'), (7, 'clubs')]]
play7 = [[(12, 'hearts'), (5, 'diamonds'), (12, 'diamonds'), (9, 'clubs'), (10, 'diamonds')], [(8, 'clubs'), (13, 'hearts'), (8, 'spades'), (6, 'diamonds'), (2, 'clubs')]]
play8 = [[(8, 'diamonds'), (12, 'clubs'), (7, 'clubs'), (6, 'spades')], [(7, 'hearts'), (2, 'diamonds'), (10, 'spades'), (11, 'spades')]]
play9 = [[(3, 'hearts'), (6, 'clubs'), (9, 'clubs'), (3, 'spades')], [(3, 'diamonds'), (2, 'diamonds'), (12, 'diamonds'), (2, 'hearts')]]
play10 = [[(3, 'clubs'), (11, 'diamonds'), (6, 'spades'), (12, 'hearts')], [(4, 'hearts'), (3, 'spades'), (7, 'diamonds'), (10, 'diamonds')]]
play11 = [[(13, 'spades'), (7, 'diamonds'), (10, 'clubs')], [(6, 'diamonds'), (8, 'diamonds'), (9, 'spades')]]
play12 = [[(9, 'diamonds'), (9, 'spades'), (6, 'diamonds')], [(3, 'hearts'), (4, 'hearts'), (4, 'diamonds')]]
play13 = [[(10, 'spades'), (12, 'hearts'), (5, 'clubs')], [(6, 'clubs'), (9, 'diamonds'), (6, 'hearts')]]
play14 = [[(9, 'spades'), (11, 'clubs'), (12, 'hearts')], [(3, 'hearts'), (13, 'diamonds'), (2, 'diamonds')]]
play15 = [[(4, 'spades'), (7, 'spades'), (3, 'diamonds')], [(11, 'spades'), (13, 'clubs'), (10, 'hearts')]]
play16 = [[(4, 'hearts'), (13, 'spades'), (6, 'spades')], [(10, 'diamonds'), (4, 'diamonds'), (12, 'spades')]]
play17 = [[(7, 'diamonds'), (13, 'diamonds'), (10, 'hearts'), (13, 'hearts'), (12, 'diamonds')], [(5, 'spades'), (9, 'hearts'), (12, 'spades'), (7, 'spades'), (8, 'clubs')]]
play18 = [[(11, 'spades'), (6, 'clubs'), (5, 'hearts'), (5, 'spades'), (2, 'spades')], [(11, 'hearts'), (4, 'clubs'), (6, 'hearts'), (12, 'clubs'), (3, 'diamonds')]]
play19 = [[(7, 'spades'), (7, 'diamonds'), (5, 'diamonds')], [(4, 'clubs'), (2, 'clubs'), (10, 'clubs')]]
play20 = [[(8, 'diamonds'), (7, 'hearts'), (4, 'diamonds'), (2, 'clubs')], [(11, 'spades'), (12, 'diamonds'), (3, 'diamonds'), (2, 'diamonds')]]

def test_winner():
    """This test verifies the value of winner function"""
    assert poker.winner(play1[0],play1[1]) == 'player2',"winner function is biased!!!!"
    assert poker.winner(play2[0],play2[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play3[0],play3[1]) == 'player2',"winner function is biased!!!!"
    assert poker.winner(play4[0],play4[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play5[0],play5[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play6[0],play6[1]) == 'player2',"winner function is biased!!!!"
    assert poker.winner(play7[0],play7[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play8[0],play8[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play9[0],play9[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play10[0],play10[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play11[0],play11[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play12[0],play12[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play13[0],play13[1]) == 'player2',"winner function is biased!!!!"
    assert poker.winner(play14[0],play14[1]) == 'player2',"winner function is biased!!!!"
    assert poker.winner(play15[0],play15[1]) == 'player2',"winner function is biased!!!!"
    assert poker.winner(play16[0],play16[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play17[0],play17[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play18[0],play18[1]) == 'player1',"winner function is biased!!!!"
    assert poker.winner(play19[0],play19[1]) == 'player2',"winner function is biased!!!!"
    assert poker.winner(play20[0],play20[1]) == 'player2',"winner function is biased!!!!"

 
    
play21 = [[(9, 'spades'), (12, 'hearts'), (2, 'spades'), (11, 'clubs')],[(4, 'spades'), (6, 'spades'), (12, 'spades'), (10, 'clubs')]]
play22 = [[(11, 'spades'), (8, 'clubs'), (9, 'clubs')],[(8, 'hearts'), (11, 'clubs'), (4, 'clubs')]]    


def test_winner_draw_cases():
    """This test verifies the value of winner function for draw case"""
    assert poker.winner(play21[0],play21[1]) == 'draw',"winner function is biased!!!!"
    assert poker.winner(play22[0],play22[1]) == 'draw',"winner function is biased!!!!"
    
    
#------------------------------tests poker-------------
possible_output=['player1','player2','draw']

def test_poker_function():
    """This test verifies one of the output of poker function"""
    player1,player2,winner = poker.poker()
    assert winner in possible_output,"poker function is not working!!!!! "


    
    
    
