from flask import Flask, request
app = Flask(__name__)

@app.route('/helloworld', methods = ['GET'])
def helloworld():
    return "Hello World!!\n"

@app.route('/hello/<name>', methods = ['GET'])
def hello_name():
    return "Hello {}\n".format(name)

@app.route('/hello', methods = ['GET'])
def hello_name1():
    print (request.args)
    for i in request.args.keys():
        print (i)
    name = request.args.get('name')
    return '(round2) Hello {}\n'.formate(name)

@app.route('/animals', methods = ['GET'])
def get_animals():
    return json.dumps(getdata())

@app.route('/animals/<name>', methods = ['GET'])


def getdata():
    with open('animals.json', 'r') as json_file:
        userdata = json.load(json_file)
    return userdata

if __name__ == 'main':
    app.run(debug=True, host='0.0.0.0')
