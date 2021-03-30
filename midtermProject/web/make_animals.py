#!/usr/bin/env python3

import json
import random
import petname
import sys
import datetime
import uuid

def make_head():
    animals = ["snake", "bull", "lion", "raven", "bunny"]
    head = animals[random.randint(0,4)]
    return head

def make_body():
    body1 = petname.name()
    body2 = petname.name()
    body = body1 + "-" + body2
    return body

def make_arms():
    arms = random.randint(1,5) * 2
    return arms

def make_legs():
    legs = random.randint(1,4) * 3
    return legs

def make_tails(arms_str, legs_str):
    tails = int(arms_str) + int(legs_str)
    return tails

def make_timestamp():
    timestamp = str(datetime.datetime.now())
    return timestamp

def make_uuid():
    id_number = str(uuid.uuid4())
    return id_number

def create_animal():
    head = make_head()
    body = make_body()
    arms = make_arms()
    legs = make_legs()
    tails = make_tails(arms, legs)
    timestamp = make_timestamp()
    id_number = make_uuid()
    animal = {'head': head, 'body': body, 'arms': arms, 'legs': legs, 'tails': tails, 'created_on': timestamp, 'uuid': id_number}
    return animal

def main():
    animals_list = {}
    animals_list['animal'] = []
    
    for i in range(0,20):
        animal = create_animal()
        animals_list['animal'].append(animal)
    return animals_list['animal']
#    with open('animals.json', 'w') as out:
#        json.dump(animals_list, out, indent=2)

if __name__ == '__main__':
     main()

