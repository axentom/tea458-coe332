import csv
import json
 
def make_json(csvFilePath, jsonFilePath):
     
    data = {}
    count = 0
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        for rows in csvReader:
            key = count
            data[key] = rows
            count = count + 1
 
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
         
csvFilePath = r'data.csv'
jsonFilePath = r'data.json'
 
make_json(csvFilePath, jsonFilePath)
