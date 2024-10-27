import random

def guesse(x):
    random_number = random.randint(1,x)
    guesse = 0
    while guesse != random_number:
        guesse = int(input(f"Guesse the number between 1 and {x} : "))
        if guesse < random_number:
            print("Your to low")
        elif guesse > random_number:
            print("Your to high")
            
    print("Wow, you get it, congrats")
    

guesse(100)