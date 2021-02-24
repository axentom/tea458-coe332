import json
import random

def main():
    with open('animals.json', 'r') as f:
        animals = json.load(f)

    print('One random animal:')
    print(animals['animal'][random.randint(0,19)])

# Construct new dict for parents
    parent1_index = random.randint(0,19)
    parent2_index = random.randint(0,19)
    while (parent2_index == parent1_index):
        parent2_index = random.randint(0,19)
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

if __name__ == "__main__":
    main()
