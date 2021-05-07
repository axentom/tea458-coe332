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
    rd = redis.StrictRedis(host = "10.110.179.174",port=6379,db=0)
    for key in data:
        rd.hmset[key, data[key]]
        count = count + 1
    rd.set('count', count)

    return "data loaded into db, count: {}\n".format(count)

# Route to pull figure

# Route to Read entry by Animal ID

# Route to Update entry by Animal ID

# Route to Delete entry by Animal ID

# Route to Create an entry in redis db
@app.route('/create/<animal_id>/<name>/<datetime>/<monthyear>/<dob>/<outcome_type>/<outcome_subtype>/<animal_type>/<sex>/<age>/<breed>/<color>', methods=['GET'])
def create(animal_id, name, datetime, monthyear, dob, outcome_type, outcome_subtype, animal_type, sex, age, breed, color):
    count = int(rd.get('count'))

    rd.hmset[count, {"Animal ID": animal_id, "Name": name, "DateTime": datetime, "MonthYear": monthyear, "Date of Birth": dob, \
    "Outcome Type": outcome_type, "Outcome Subtype": outcome_subtype, "Animal Type": animal_type, "Sex upon Outcome": sex, \
    "Age upon Outcome": age, "Breed": breed, "Color": color}]

    count = count + 1
    rd.set('count', count)
    return "created new entry for Animal ID: {}\n".format(animal_id)

@app.route('/jobs', methods=['POST'])
def jobs_api():
    try:
        job = request.get_json(force=True)
    except Exception as e:
        return True, json.dumps({'status': "Error", 'message': 'Invalid JSON: {}.'.format(e)})
    return json.dumps(jobs.add_job(job['start'], job['end']))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
