# api.py
import json
from flask import Flask, request
import jobs

app = Flask(__name__)

# Route to load data into redis db
@app.route('/loaddata', methods=['GET'])
def data():
    with open("data.json","r") as json_data:
        data = json.load(json_data)

    count = 0
    rd = jobs.rd
    for key in data:
        rd.hmset[key, data[key]]
        count = count + 1
    rd.set('count', count)

    return "data loaded into db, count: {}\n".format(count)

# Route to pull all data
@app.route('/get', methods = ['GET'])
def get():
    out = get_data()
    return out

# Route to pull figure

# Route to Read entry by Animal ID
@app.route('/read/<id_no>', methods = ['GET'])
def read():
    count = int(rd.get('count'))
    animals_dict = get_data()
    animal = 'Error: No animals matching that uuid\n'
    for i in range(0, count):
        if animals_dict[i]['Animal ID'] == id_no:
            animal = json.dumps(animals_dict[i]) + "\n"
    return animal

# Route to Update entry by Animal ID
@app.route('/read/<id_no>/update/<key>/<new_value>', methods = ['GET'])
def update(id_no, key, new_value):
    count = int(rd.get('count'))
    animals_dict = get_data()
    animal = 'Error: No animals matching that Animal ID\n'
    for i in range(0, count):
        if animals_dict[i]['Animal ID'] == id_number:
            rd.hset(i, key, new_value)
            animals_dict[i][key] = new_value
            animal = json.dumps(animals_dict[i]) + "\n"
    return animal

# Route to Delete entry by Animal ID
@app.route('/delete/id_no', methods = ['GET'])
def delete(id_no):
    count = int(rd.get('count'))
    animals_dict = get_data()
    return_dict = {}
    assigner = 0
    for i in range(0, count):
        argument_id = animals_dict[i]['Animal ID']
        if argument_id != id_no:
            return_dict[assigner] = animals_dict[i]
            assigner = assigner + 1
    count = count - 1
    rd.set('count', count)
    for j in range(0, count):
        rd.hmset(j, return_dict[j])
    rd.del(count + 1)

# Route to Create an entry in redis db
@app.route('/create/<id_no>/<name>/<datetime>/<monthyear>/<dob>/<outcome_type>/<outcome_subtype>/<animal_type>/<sex>/<age>/<breed>/<color>', methods=['GET'])
def create(id_no, name, datetime, monthyear, dob, outcome_type, outcome_subtype, animal_type, sex, age, breed, color):
    count = int(rd.get('count'))

    rd.hmset[count, {"Animal ID": id_no, "Name": name, "DateTime": datetime, "MonthYear": monthyear, "Date of Birth": dob, \
    "Outcome Type": outcome_type, "Outcome Subtype": outcome_subtype, "Animal Type": animal_type, "Sex upon Outcome": sex, \
    "Age upon Outcome": age, "Breed": breed, "Color": color}]

    count = count + 1
    rd.set('count', count)
    return "created new entry for Animal ID: {}\n".format(id_no)

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

def get_data():
    animals = {}
    length = int.(rd.get('count'))
    for i in range(0, length):
        animals[i] = rd.hgetall(i)
    return animals

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
