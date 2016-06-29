import json
from os import listdir, getcwd

# extracts json data
def getJsonData():
    files = listdir(getcwd() + '/modules/documentLearning/json')
    json_data = []
    for file in files:
     with open(getcwd() + '/modules/documentLearning/json/' + file) as json_file:
         j = json.load(json_file)
         json_data.append(j)
    return json_data






