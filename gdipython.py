#name = input('What is your name?')
##age = input('What is your age?')
#ok = input('Did you find everything ok? ')
#name = input('what is your name? ')
#bags = input('Do you want paper or plastic? ')
#total = input ('What is your total ')
#number_total = float(total)
#sales_tax = number_total * .0825
#total_w_tax = number_total + sales_tax
#print("your total is $" + str(total_w_tax) )


#boolean expressions


# ### defined with brackets and commas between
# food = []
# #food.append('tacos')
# food.append('chicken')
# food.append("beef")
# #print(food)
# #print(food[0])
# len(food)
# ###

# print("It's your birthday")
# age = input("How old are you? ")
# int_age = int(age)
# if int_age < 21:
#     print ("you may not have a beer!")
# else:
#     beers = input('How many beers did you have? ')
#     beers_int = int(beers)
#
#     if beers_int > 3:
#         print("you're drunk!")
#     elif beers_int > 1:
#         print("you have room for more!")
#     else:
#         print("have a good one")

# number = input('give me a number: ')
# int_number= int(number)
# if int_number > 0:
#     print(it is positive!')
# elif int_number < 0:
#     print('it is negavive')
# else:

# shipping_cost = 2.5
# prices = [1.00, 4.23, 5.44]
#
# print("-"  * 30)
#
# for price in prices:
#     print('price: ' + str(prices))
#     print("price with shipping " +
#             str(price + shipping_cost) )
#     print("-" * 30)

# for num in range( 10, 1, -2):
#     print(num)
#     print ("*" * 10)
#
# words  = ["mary", "had", "a", "little", "lamb"]
#
# for word in words:
#     if len(word) == 4:
#         print(word)

#start example from class
# number_to_guess  = "5"

# user_guess = "500"

# while user_guess != number_to_guess:
#     user_guess = input("What is my number? ")
#     print ("You guessed: " + user_guess)

#     if user_guess == number_to_guess:
#         print("You win!!")
#     else:
#         print('Your guess is wrong! Try again!')

#New Attempt at modification
#import random package and use randint to pick a random number for the number to guess value
import random 
number_to_guess  = random.randint(1, 10)

user_guess = "500"

while user_guess != number_to_guess:
    user_guess = int(input("What is my number? "))
    print ("You guessed: " + str(user_guess))

    if user_guess == number_to_guess:
        print("You win!!")
    elif user_guess < number_to_guess:
         print("Your number is too low")
    elif user_guess > number_to_guess:
        print("Your guess is too high!")
    else:
        print("wrong try again!")
    