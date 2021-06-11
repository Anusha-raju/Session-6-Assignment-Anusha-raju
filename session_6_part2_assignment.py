""" Session 6 - assignment 2"""
from math import sqrt
from math import exp
from functools import reduce
from functools import partial
from random import randint

###########----Question 1--------############
def number_fibonacci(number:'int')->'bool':
    """ This function returns True if number is a fibonacci number 
    INPUT:
        number : int : user input
    OUTPUT:
        True if number is a fibonacci number else False
        
    Fibonacci number: when [5*number*number + 4  or 5*number*number - 4] is a perfect square 
    """
    if int(number) == number:
        return bool(list(filter(lambda num: pow(int(sqrt(num)),2) == num ,[5*number*number + 4 , 5*number*number - 4])))
    else: #if number is not of int type
        raise TypeError("Number should be of Integer type")
        
##############--------Question 2--------############
def add_a_b(list_a:'list',list_b:'list')->'list':
    """ This function returns a list a sum of a and b where a is even numbers from list_a & b is odd numbers from list_b
    INPUT:
        list_a : list of integers
        list_b : list of integers
    OUTPUT:
        list of sum of a and b where a is even numbers from list_a and b is odd numbers from list_b
    """
    if type(list_a) and type(list_b) is list:
        return [x+y for x,y in zip(list_a,list_b) if x%2==0 and y%2!=0]
    else: #if list-a or list-b is not a list
        raise TypeError("Invaid Input:Enter valid inputs of type {list}")
        


def vowel_eraser(string:'str')->'str':
    """ This function returns a string eliminating the vowels
    INPUT: string
    OUTPUT: string without vowels (a,e,i,o,u)
    """
    if type(string) == str:
        return ("".join([x for x in string if x.lower() not in ['a','e','i','o','u']]))
    else: #if string is not a vowel
        raise TypeError("Invalid Input: Enter a String")
         

def sigmoid(array:'list')->'list':
    """ This function returns a list of sigmoid values of array list
    INPUT:
        array : list
    OUTPUT:
        list of sigmoid values
        
    SIGMOID FUNCTION = 1/1+e^(-x)  : x can be int or float
    """
    return [1/(1 + exp(-x)) for x in array if type(x) is int or float]

def shift_by_n(string:'str',n:'int' = 5)->'str':
    """ This function shifts the character by n according to ascii values
    INPUT: 
        string : 'str'
        n : int : default = 5
    OUTPUT:
        string shifted by n characters
    ASCII values: a = 97 to z = 122
    """
    return ''.join([chr(((ord(x.lower())+n-97)%26)+97) for x in string])


#############---------Question 3------------###################
def check_swear_words(para:'str')->'bool':
    """ This function checks if there are any swear words in the paragraph
    INPUT:
        para: 'str' : len(para)>200
    OUTPUT:
        'bool': True if swear word is present else False 
    """
    #words list has all the swear words
    words = ['4r5e', '5h1t', '5hit', 'a55', 'anal', 'anus', 'ar5e', 'arrse', 'arse', 'ass', 'ass-fucker', 'asses', 'assfucker', 'assfukka', 'asshole', 'assholes', 'asswhole', 'a_s_s', 'b!tch', 'b00bs', 'b17ch', 'b1tch', 'ballbag', 'balls', 'ballsack', 'bastard', 'beastial', 'beastiality', 'bellend', 'bestial', 'bestiality', 'bi+ch', 'biatch', 'bitch', 'bitcher', 'bitchers', 'bitches', 'bitchin', 'bitching', 'bloody', 'blow job', 'blowjob', 'blowjobs', 'boiolas', 'bollock', 'bollok', 'boner', 'boob', 'boobs', 'booobs', 'boooobs', 'booooobs', 'booooooobs', 'breasts', 'buceta', 'bugger', 'bum', 'bunny fucker', 'butt', 'butthole', 'buttmunch', 'buttplug', 'c0ck', 'c0cksucker', 'carpet muncher', 'cawk', 'chink', 'cipa', 'cl1t', 'clit', 'clitoris', 'clits', 'cnut', 'cock', 'cock-sucker', 'cockface', 'cockhead', 'cockmunch', 'cockmuncher', 'cocks', 'cocksuck ', 'cocksucked ', 'cocksucker', 'cocksucking', 'cocksucks ', 'cocksuka', 'cocksukka', 'cok', 'cokmuncher', 'coksucka', 'coon', 'cox', 'crap', 'cum', 'cummer', 'cumming', 'cums', 'cumshot', 'cunilingus', 'cunillingus', 'cunnilingus', 'cunt', 'cuntlick ', 'cuntlicker ', 'cuntlicking ', 'cunts', 'cyalis', 'cyberfuc', 'cyberfuck ', 'cyberfucked ', 'cyberfucker', 'cyberfuckers', 'cyberfucking ', 'd1ck', 'damn', 'dick', 'dickhead', 'dildo', 'dildos', 'dink', 'dinks', 'dirsa', 'dlck', 'dog-fucker', 'doggin', 'dogging', 'donkeyribber', 'doosh', 'duche', 'dyke', 'ejaculate', 'ejaculated', 'ejaculates ', 'ejaculating ', 'ejaculatings', 'ejaculation', 'ejakulate', 'f u c k', 'f u c k e r', 'f4nny', 'fag', 'fagging', 'faggitt', 'faggot', 'faggs', 'fagot', 'fagots', 'fags', 'fanny', 'fannyflaps', 'fannyfucker', 'fanyy', 'fatass', 'fcuk', 'fcuker', 'fcuking', 'feck', 'fecker', 'felching', 'fellate', 'fellatio', 'fingerfuck ', 'fingerfucked ', 'fingerfucker ', 'fingerfuckers', 'fingerfucking ', 'fingerfucks ', 'fistfuck', 'fistfucked ', 'fistfucker ', 'fistfuckers ', 'fistfucking ', 'fistfuckings ', 'fistfucks ', 'flange', 'fook', 'fooker', 'fuck', 'fucka', 'fucked', 'fucker', 'fuckers', 'fuckhead', 'fuckheads', 'fuckin', 'fucking', 'fuckings', 'fuckingshitmotherfucker', 'fuckme ', 'fucks', 'fuckwhit', 'fuckwit', 'fudge packer', 'fudgepacker', 'fuk', 'fuker', 'fukker', 'fukkin', 'fuks', 'fukwhit', 'fukwit', 'fux', 'fux0r', 'f_u_c_k', 'gangbang', 'gangbanged ', 'gangbangs ', 'gaylord', 'gaysex', 'goatse', 'God', 'god-dam', 'god-damned', 'goddamn', 'goddamned', 'hardcoresex ', 'hell', 'heshe', 'hoar', 'hoare', 'hoer', 'homo', 'hore', 'horniest', 'horny', 'hotsex', 'jack-off ', 'jackoff', 'jap', 'jerk-off ', 'jism', 'jiz ', 'jizm ', 'jizz', 'kawk', 'knob', 'knobead', 'knobed', 'knobend', 'knobhead', 'knobjocky', 'knobjokey', 'kock', 'kondum', 'kondums', 'kum', 'kummer', 'kumming', 'kums', 'kunilingus', 'l3i+ch', 'l3itch', 'labia', 'lmfao', 'lust', 'lusting', 'm0f0', 'm0fo', 'm45terbate', 'ma5terb8', 'ma5terbate', 'masochist', 'master-bate', 'masterb8', 'masterbat*', 'masterbat3', 'masterbate', 'masterbation', 'masterbations', 'masturbate', 'mo-fo', 'mof0', 'mofo', 'mothafuck', 'mothafucka', 'mothafuckas', 'mothafuckaz', 'mothafucked ', 'mothafucker', 'mothafuckers', 'mothafuckin', 'mothafucking ', 'mothafuckings', 'mothafucks', 'mother fucker', 'motherfuck', 'motherfucked', 'motherfucker', 'motherfuckers', 'motherfuckin', 'motherfucking', 'motherfuckings', 'motherfuckka', 'motherfucks', 'muff', 'mutha', 'muthafecker', 'muthafuckker', 'muther', 'mutherfucker', 'n1gga', 'n1gger', 'nazi', 'nigg3r', 'nigg4h', 'nigga', 'niggah', 'niggas', 'niggaz', 'nigger', 'niggers ', 'nob', 'nob jokey', 'nobhead', 'nobjocky', 'nobjokey', 'numbnuts', 'nutsack', 'orgasim ', 'orgasims ', 'orgasm', 'orgasms ', 'p0rn', 'pawn', 'pecker', 'penis', 'penisfucker', 'phonesex', 'phuck', 'phuk', 'phuked', 'phuking', 'phukked', 'phukking', 'phuks', 'phuq', 'pigfucker', 'pimpis', 'piss', 'pissed', 'pisser', 'pissers', 'pisses ', 'pissflaps', 'pissin ', 'pissing', 'pissoff ', 'poop', 'porn', 'porno', 'pornography', 'pornos', 'prick', 'pricks ', 'pron', 'pube', 'pusse', 'pussi', 'pussies', 'pussy', 'pussys ', 'rectum', 'retard', 'rimjaw', 'rimming', 's hit', 's.o.b.', 'sadist', 'schlong', 'screwing', 'scroat', 'scrote', 'scrotum', 'semen', 'sex', 'sh!+', 'sh!t', 'sh1t', 'shag', 'shagger', 'shaggin', 'shagging', 'shemale', 'shi+', 'shit', 'shitdick', 'shite', 'shited', 'shitey', 'shitfuck', 'shitfull', 'shithead', 'shiting', 'shitings', 'shits', 'shitted', 'shitter', 'shitters ', 'shitting', 'shittings', 'shitty ', 'skank', 'slut', 'sluts', 'smegma', 'smut', 'snatch', 'son-of-a-bitch', 'spac', 'spunk', 's_h_i_t', 't1tt1e5', 't1tties', 'teets', 'teez', 'testical', 'testicle', 'tit', 'titfuck', 'tits', 'titt', 'tittie5', 'tittiefucker', 'titties', 'tittyfuck', 'tittywank', 'titwank', 'tosser', 'turd', 'tw4t', 'twat', 'twathead', 'twatty', 'twunt', 'twunter', 'v14gra', 'v1gra', 'vagina', 'viagra', 'vulva', 'w00se', 'wang', 'wank', 'wanker', 'wanky', 'whoar', 'whore', 'willies', 'willy', 'xrated', 'xxx']
    if len(para.split())<200:
        raise TypeError("This is not a paragraph")
    else:
        return any([False if word.lower() not in words else True for word in para.split()])


##############-----------Question 4-----------------###############
def add_even_numbers(lists:'list')->'int':
    """ This function adds all the even numbers in the list
    INPUT: list
    OUTPUT:
        int: sum of even numbers
    """
    return reduce(lambda a,b:a+b,[x for x in lists if x%2==0])

def highest_ascii_char(string:'str')->'str':
    """ This function returns the character with highest ascii value
    INPUT: string
    OUTPUT: 
        string with highest ascii value
    """
    return reduce(lambda a,b:a if ord(a)>ord(b) else b,string)

def add_third_number(lists:'list')->'int':
    """ This function adds every third number in a list
    INPUT: list
    OUTPUT:
        int: sum of every third element in the list
    """
    return reduce(lambda a,b: a+b,lists[2::3])

#############--------------Question 5-------------#############
def number_plates(limit:'int' = 15)->'list':
    """ This function returns list of n{limit: default=15} random number plates of the type KA DD AA DDDD 
    where 'KA' is state code
           DD is 10<=DD<=99
           AA is which a string from AA to ZZ
           DDDD is 1000<=DDDD<=9999
    """
    return(['KA'+str(randint(10,99))+chr(randint(65,90))+chr(randint(65,90))+str(randint(1000,9999)) for x in range(limit)])
    
##############---------------Question 6--------------################   
def number_plates_user_choice(state_code:'str', last_digit_start:'int' = 1000, last_digit_end:'int' = 9999, limit:'int' = 15)->'list':
    """ This function returns list of n{limit: default = 5} random number plates of the type AA DD AA DDDD 
    where 'AA' is state code
           DD is 10<=DD<=99
           AA is which a string from AA to ZZ
           DDDD is 1000<=DDDD<=9999
    
    INPUT :
        state_code : string {'KA','DL'}
        last_digit_start: int : default = 1000: should be greater than or equal to 1000 & less than last_digit_end
        last_digit_end: int : default = 9999: should be less then or equal to 9999
        limit: int : default = 15
        
    OUTPUT:
        list of number plates as user choice
    """
    if isinstance(state_code, str) and len(state_code)==2: #checks the state code validity
        if last_digit_start>=1000 and last_digit_end<=9999 and last_digit_start<last_digit_end: #checks the range of DDDD validity
            return ([state_code.upper()+str(randint(10, 99))+chr(randint(65,90))+chr(randint(65,90))+str(randint(last_digit_start,last_digit_end)) for x in range(limit)])
        else:
            raise ValueError("Enter proper range of last digits")
    else:
        raise TypeError("Enter a valid state code")
        
        
#partial function        
number_plate_partial = partial(number_plates_user_choice,last_digit_start = 1000,last_digit_end = 9999) #partial function of number_plates_user_choice
