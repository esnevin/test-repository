'''Write a program that will generate a random playing card e.g. ‘9 Hearts’, ‘Queen Spades’ when the return key is pressed. Rather than generate a random number from 1 to 52. Create two random numbers – one for the suit and one for the card. '''

import random

suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
card = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

random_card = random.choice(card)
random_suit = random.choice(suit)

print("Your card is {} of {}".format(random_card, random_suit)) 
