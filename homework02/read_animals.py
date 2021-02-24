import json
import random
import sys

def check_animals_dict_length(): # Check to see if animals.json has enough values in it to breed
    with open('animals.json', 'r') as f:
        animals = json.load(f)
    count = len(animals['animal'])
    if (count < 2):
        return('animals dict length FAIL')
        sys.exit()
    else:
        return('animals dict length pass')

def check_parents_index_range(parent1_index, parent2_index): # Checks that the input indices are within the range of animals.json
    with open('animals.json', 'r') as f:
        animals = json.load(f)
    count = len(animals['animal'])
    if (parent1_index not in range(0,count)):
        return(f'Parent 1 index: {parent1_index} range FAIL')
        sys.exit()
    elif (parent2_index not in range(0,count)):
        return(f'Parent 2 index: {parent2_index} range FAIL')
        sys.exit()
    else:
        return(f'Parent indices: {parent1_index} and {parent2_index} range pass')

def create_children(parent1_index, parent2_index):
    with open('animals.json', 'r') as f:
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
    with open('animals.json', 'r') as f:
        animals = json.load(f)

    print('One random animal:')
    print(animals['animal'][random.randint(0,19)])

def main():
    p1 = int(sys.argv[1])
    p2 = int(sys.argv[2])
    
    print(check_animals_dict_length())
    print(check_parents_index_range(p1,p2))
    random_animal()
    create_children(p1,p2)

if __name__ == "__main__":
    main()
