import json
import random
import petname

""" 
This Function picks a random head for Dr. Moreau's beast
"""
def make_head():
    animals = ["snake", "bull", "lion", "raven", "bunny"]
    head = animals[random.randint(0,4)]
    return head

"""
This Function pulls two random animals from the petname library and mashes their bodies together for Dr. Moreau's beast
"""
def make_body():
    body1 = petname.name()
    body2 = petname.name()
    body = body1 + "-" + body2
    return body

"""
This Function creates an even number between 2-10 inclusive to be the number of arms in Dr. Moreau's beast
"""
def make_arms():
    arms = random.randint(1,5) * 2
    return arms

"""
This function creates a multiple of three between 3-12 inclusive to be the nuber of legs in Dr. Moreau's beast
"""
def make_legs():
    legs = random.randint(1,4) * 3
    return legs

"""
This function creates a non-random number of tails equal to the sum of arms and legs
This function REQUIRES the presence of a legs and arms int variable
"""
def make_tails(arms_str, legs_str):
    tails = int(arms_str) + int(legs_str)
    return tails

def create_animal():
    head = make_head()
    body = make_body()
    arms = make_arms()
    legs = make_legs()
    tails = make_tails(arms, legs)
    animal = {'head': head, 'body': body, 'arms': arms, 'legs': legs, 'tails': tails}
    return animal

def main():
    animals_list = {}
    animals_list['animal'] = []
    
    for i in range(0,20):
        animal = create_animal()
        animals_list['animal'].append(animal)
    
    with open('animals.json', 'w') as out:
        json.dump(animals_list, out, indent=2)

if __name__ == '__main__':
     main()

