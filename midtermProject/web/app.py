import json
import redis
import datetime
import make_animals
from flask import Flask, request

app = Flask(__name__)

rd = redis.StrictRedis(host='axentom-redis', port=6379, db=0)

@app.route('/', methods = ['GET'])
def helloworld():
    return "Try routes like: /reset/20 or /get\n"

@app.route('/<invalid>', methods = ['GET'])
def invalid_catcher(invalid):
    return "{} is an invalid route\n".format(invalid)

# Reset data (Takes arg input for number of animals to reset to)
@app.route('/reset/<arg>', methods = ['GET'])
def reset_animals(arg):
    arg = int(arg)
    rd.set('count', arg)
    for i in range(0, arg):
        animal = make_animals.create_animal()
        rd.hmset(i, animal)
    return "Animals data in Redis DB reset; count: {}\n".format(arg)

# Retrieve total data
@app.route('/get', methods = ['GET'])
def get_animals():
    out = get_data()
    return out 

# Select a creature by UUID
@app.route('/uuid/<id_number>', methods = ['GET'])
def get_by_uuid(id_number):
    count = int(rd.get('count'))
    animals_dict = get_data()
    animal = 'Error: No animals matching that uuid\n'
    for i in range(0, count):
        if animals_dict[i]['uuid'] == id_number:
            animal = json.dumps(animals_dict[i]) + "\n"
    return animal

# Edit a creature by UUID
@app.route('/uuid/<id_number>/edit/<key>/<new_value>', methods = ['GET'])
def edit_by_uuid(id_number, key, new_value):
    count = int(rd.get('count'))
    animals_dict = get_data()
    animal = 'Error: No animals matching that uuid\n'
    for i in range(0, count):
        if animals_dict[i]['uuid'] == id_number:
            rd.hset(i, key, new_value)
            animals_dict[i][key] = new_value
            animal = json.dumps(animals_dict[i]) + "\n"
    return animal

# Select creatures by date range
@app.route('/date/<start>/<end>', methods = ['GET'])
def get_by_date(start, end):
    count = int(rd.get('count'))
    animals_dict = get_data()
    return_dict = {}
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d_%H:%M:%S.%f")
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d_%H:%M:%S.%f")
    assigner = 0
    for i in range(0, count):
        argument_date = datetime.datetime.strptime(animals_dict[i]['created_on'], "%Y-%m-%d %H:%M:%S.%f")
        if (start_date <= argument_date <= end_date):
            return_dict[assigner] = animals_dict[i]
            assigner += 1
    return return_dict

# Delete a selection of animals by date range
@app.route('/delete/date/<start>/<end>', methods = ['GET'])
def delete_by_date(start, end):
    count = int(rd.get('count'))
    animals_dict = get_data()
    return_dict = {}
    start_date = datetime.datetime.strptime(start, "%Y-%m-%d_%H:%M:%S.%f")
    end_date = datetime.datetime.strptime(end, "%Y-%m-%d_%H:%M:%S.%f")
    assigner = 0
    for i in range(0, count):
        argument_date = datetime.datetime.strptime(animals_dict[i]['created_on'], "%Y-%m-%d %H:%M:%S.%f")
        if not (start_date <= argument_date <= end_date):
            rd.hmset(assigner, animals_dict[i])
            assigner += 1
    # Here write clean up and count adjustment 
    rd.set('count', assigner)
    count_cleanup(100)
    return 'Animals created within input datetime range have been deleted\n'

# Return the average number of legs per animal
@app.route('/averagelegs', methods = ['GET'])
def average_legs():
    count = int(rd.get('count'))
    total_legs = 0
    for i in range(0, count):
        total_legs += float(rd.hget(i, 'legs'))
    average = total_legs / float(count)
    return 'Average legs per animal: ' + str(average) + '\n'

# Retrieve current count
@app.route('/count', methods = ['GET'])
def count_animals():
    length = rd.get('count')
    count = "Number of animals: " + length + "\n"
    return count

# Delete specific entry
@app.route('/delete/pair/<hash_no>/<key>', methods = ['GET'])
def delete_kv_pair(hash_no, key):
    rd.hdel(hash_no, key)
    str1 = 'Deleted from hash {}: '.format(hash_no)
    str2 = 'pair at key "{}"'.format(key)
    return str1 + str2 + '\n'

def get_data():
    animals = {}
    length = int(rd.get('count'))
    for i in range(0, length):
        animals[i] = rd.hgetall(i)
    return animals

def count_cleanup(max):
    count = int(rd.get('count'))
    for i in range(count, max):
        rd.hdel(i, 'arms')
        rd.hdel(i, 'body')
        rd.hdel(i, 'created_on')
        rd.hdel(i, 'head')
        rd.hdel(i, 'legs')
        rd.hdel(i, 'uuid')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


