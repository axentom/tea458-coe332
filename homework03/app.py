import generate_animals
import json
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def helloworld():
    return "Hello World!!\n"

@app.route('/hello/<name>', methods = ['GET'])
def hello_name(name):
    return "Hello {}\n".format(name)

@app.route('/hello', methods = ['GET'])
def hello_name1():
    print (request.args)
    for i in request.args.keys():
        print (i)
    name = request.args.get('name')
    return 'Hello {}\n'.format(name)

@app.route('/makeanimals', methods = ['GET'])
def make_animals():
    generate_animals.main()
    return json.dumps(get_data())

@app.route('/animals', methods = ['GET'])
def get_animals():
    return json.dumps(get_data())

def get_data():
    with open('animals.json', 'r') as json_file:
        userdata = json.load(json_file)
    return userdata

@app.route('/animals/head/<head>', methods = ['GET'])
def get_data_head(head):
    with open('animals.json', 'r') as json_file:
        userdata = json.load(json_file)
    print(type(userdata))
    jsonList = userdata['animal']
    print(type(jsonList))
    output = [x for x in jsonList if x['head'] == '{}'.format(head)]
    print(type(output))
    return json.dumps(output)

@app.route('/animals/legs/<legs>', methods = ['GET'])
def get_data_legs(legs):
    with open('animals.json', 'r') as json_file:
        userdata2 = json.load(json_file)
    print(type(userdata2))
    jsonList2 = userdata2['animal']
    print(type(jsonList2))
    output2 = [y for y in jsonList2 if y['legs'] == int(legs)]
    print(type(output2))
    return json.dumps(output2)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


