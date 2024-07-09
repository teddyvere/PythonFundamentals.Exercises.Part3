from random import randrange

print("Guess a number between 1 and 10 ")

rand_number = randrange(10)
user_number = input()


def random_number(rand_number):
    print("The random number was " + str(rand_number))

def provide_number(user_number):
    print("You gueesed " + user_number)

def eval_rand_number(rand_number, user_number):
        if int(rand_number) < int(user_number):
             print("Higher")
        if int(rand_number) > int(user_number):
             print("Lower")
        elif int(rand_number) == int(user_number):
             print("Congrats you win")     

random_number(rand_number)
provide_number(user_number)
eval_rand_number(rand_number, user_number)