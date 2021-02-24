#!/usr/bin/env python3

import json
import random
import sys

def check_parents_index_type(parent_index): # Checks to see if input parent index can be converted to type int
    try:
        int(parent_index)
        return(f'Parent index: {parent_index} type pass')
    except ValueError:
        return(f'Parent index: {parent_index} type FAIL')

def check_animals_dict_length(): # Check to see if animals.json has enough values in it to breed
    with open(sys.argv[1], 'r') as f:
        animals = json.load(f)
    count = len(animals['animal'])
    if (count < 2):
        return('animals dict length FAIL')
    else:
        return('animals dict length pass')

def check_parents_index_range(parent1_index, parent2_index): # Checks that the input indices are within the range of animals.json
    with open(sys.argv[1], 'r') as f:
        animals = json.load(f)
    count = len(animals['animal'])
    if (parent1_index not in range(0,count)):
        return(f'Parent 1 index: {parent1_index} range FAIL')
    elif (parent2_index not in range(0,count)):
        return(f'Parent 2 index: {parent2_index} range FAIL')
    else:
        return(f'Parent indices: {parent1_index} and {parent2_index} range pass')

def create_children(parent1_index, parent2_index):
    with open(sys.argv[1], 'r') as f:
        animals = json.load(f)

# Grab parents from input indices
    parents_list = {}
    parents_list['animal'] = []
    parents_list['animal'].append(animals['animal'][parent1_index])
    parents_list['animal'].append(animals['animal'][parent2_index])

# Decide on which qualities the child recieves
    headgene = random.randint(0,1)
    child_head = parents_list['animal'][headgene]['head']
    bodygene = random.randint(0,1)
    child_body = parents_list['animal'][bodygene]['body']
    armsgene = random.randint(0,1)
    child_arms = parents_list['animal'][armsgene]['arms']
    legsgene = random.randint(0,1)
    child_legs = parents_list['animal'][legsgene]['legs']
    tailsgene = random.randint(0,1)
    child_tails = parents_list['animal'][tailsgene]['tails']

# Construct child from genes and parent dict
    child_list = {}
    child_list['animal'] = []
    child = {'head': child_head, 'body': child_body, 'arms': child_arms, 'legs': child_legs, 'tails': child_tails}
    child_list['animal'].append(child)

# Output
    print('\nParent 1:')
    print(parents_list['animal'][0])
    print('\nParent 2:')
    print(parents_list['animal'][1])
    print('\nChild of the two random parents:')
    print(child_list['animal'][0])

def random_animal():
    with open(sys.argv[1], 'r') as f:
        animals = json.load(f)

    print('One random animal:')
    print(animals['animal'][random.randint(0,19)])

def main():
# Recieve inputs and check type
    p1 = (sys.argv[2])
    p2 = (sys.argv[3])
    print(check_parents_index_type(p1))
    print(check_parents_index_type(p2))
# Convert inputs to int
    p1_int = int(p1)
    p2_int = int(p2)
# Check length of animals.json
    print(check_animals_dict_length())
# Check parent indices are in range of animals.json
    print(check_parents_index_range(p1_int,p2_int))
# Create outputs
    random_animal()
    create_children(p1_int,p2_int)

if __name__ == "__main__":
    main()
