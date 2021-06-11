---
typora-copy-images-to: ./
---

# Session 6 

### Assignment 1:

```
values = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '10' , 'jack' , 'queen' , 'king' , 'ace' ]`
```

```
`suits = [ 'spades' , 'clubs' , 'hearts' , 'diamonds' ]
```

![poker_rules](poker_rules.jpg)





1. Write a single expression that includes lambda, zip, and map functions to create 52 cards in a deck 
2. Write a normal function without using lambda, zip, and map function to create 52 cards in a deck 
3. Write a function that, when given 2 sets of 3 or 4 or 5 cards (1 game can only have 3 cards with each player or 4 cards or 5 cards per player) (1 deck of cards only), (2 players only), can identify who won the game of poker. 

### Solution:

|            Function            |                        Functionality                         |
| :----------------------------: | :----------------------------------------------------------: |
| create_deck_list_comprehension |    This function creates a deck using list comprehensions    |
|          create_deck           | This function creates a deck without using list comprehensions |
|        transform_cards         |  This function changes the type of value from string to int  |
|          check_suits           | This function checks if the cards are of the same suits            (spades, clubs, diamond, hearts) |
|         check_sequence         |     This function checks if the cards are in a sequence      |
|          kind_counter          |    This function counts the kind of each card in the list    |
|        cards_evaluation        |       This function evaluates the cards of the players       |
|             winner             |         This function returns the winner of the game         |
|             poker              | This function plays the game poker with 2 players and one deck |



### Test cases:

|                       Tests                        |                          Validation                          |
| :------------------------------------------------: | :----------------------------------------------------------: |
|            test_session6_readme_exists             |                 Checks if README file exists                 |
|           test_session6_readme_500_words           |       Checks if README file has a minimum of 500 words       |
|      test_session6_readme_proper_description       | Checks if README file has description of all the functions/classes. |
| test_session6_readme_file_for_more_than_10_hashes  | Checks if README file has proper formatting (minimum of 10 hashes) |
|             test_session6_indentations             |             Checks for indentations in poker.py              |
|     test_session6_function_name_had_cap_letter     |     Checks if Capital letter(s) used for function names      |
|                test_function_count                 |    tests number of test function > 20 in test_poker file     |
|             test_function_repeatations             |        tests if any repeated tests in test_poker file        |
|     test_check_create_deck_list_comprehension      | checks the deck created using create_deck_list_comprehension function |
|               test_check_create_deck               |      checks the deck created using create_deck function      |
|    test_check_transform_cards_with_no_arguments    |           checks transform_cards with no arguments           |
|             test_check_transform_cards             |         checks transform_cards with proper arguments         |
| test_check_transform_cards_for_inappropriate_cards |        checks transform_cards with improper arguments        |
|       test_check_sequence_with_no_arguments        |           checks check_sequence with no arguments            |
|         test_check_sequence_for_a_sequence         |    checks check_sequence with proper sequential arguments    |
|       test_check_sequence_for_not_a_sequence       |     checks check_sequence with non-sequential arguments      |
|         test_check_suits_with_no_arguments         |             checks check_suits with no arguments             |
|        test_check_suits_for_different_suits        |       checks check_suits with list of different suits        |
|          test_check_suits_for_same_suits           |          checks check_suits with list of same suits          |
|                 test_kind_counter                  |    This test verifies the value of kind_counter function     |
|               test_cards_evaluation                |  This test verifies the value of cards_evaluation function   |
|                    test_winner                     |       This test verifies the value of winner function        |
|               test_winner_draw_cases               | This test verifies the value of winner function for draw case |
|                test_poker_function                 |    This test verifies one of the output of poker function    |





# Assignment 2:



1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 
2. Using list comprehension (and zip/lambda/etc if required) write expressions that:
   1. add 2 iterables a and b such that a is even and b is odd
   2. strips every vowel from a string provided (tsai>>t s)
   3. acts like a sigmoid function for a 1D array
   4. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
3. A list comprehension expression that takes a ~200-word paragraph, and checks whether it has any of the swear words 
4. Using reduce function:
   1. add only even numbers in a list
   2. find the biggest character in a string (printable ASCII characters)
   3. adds every 3rd number in a list
5. Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999 
6. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided



### Solution:

|         Function          |                        Functionality                         |
| :-----------------------: | :----------------------------------------------------------: |
|     number_fibonacci      |  This function returns True if number is a fibonacci number  |
|          add_a_b          | This function returns a list a sum of a and b where a is even numbers from list_a & b is odd numbers from list_b |
|       vowel_eraser        |    This function returns a string eliminating the vowels     |
|          sigmoid          | This function returns a list of sigmoid values of array list |
|        shift_by_n         | This function shifts the character by n {default = 5} according to ascii values |
|     check_swear_words     | This function checks if there are any swear words in the paragraph |
|     add_even_numbers      |     This function adds all the even numbers in the list      |
|    highest_ascii_char     | This function returns the character with highest ascii value |
|     add_third_number      |       This function adds every third number in a list        |
|       number_plates       | This function returns list of n{limit: default=15} random number plates of the type KA DD AA DDDD |
| number_plates_user_choice | This function returns list of n{limit: default = 5} random number plates of the type AA DD AA DDDD ,where 'AA' is state code |
|   number_plate_partial    |        partial function of number_plates_user_choice         |





