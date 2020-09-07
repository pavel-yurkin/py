
import json
import sys

json_data = { 
        "data_dict": {
            "element_one": ["hello1", "hello2", "hello3"],
            "element_two": ["echo1", "echo2"],
            "element_three": ["azaza1"]
            }
        }

data_one = dict()
data_one['Hello2'] = list()
data_one['Hello2'].append('value2')
data_one['Hello2'].append('value1')
if 'value2' not in data_one['Hello2']:
    data_one['Hello2'].append('value2')
print(data_one)

my_dict = json.dumps(json_data)

with open('hello2.txt', 'w') as f:
    json.dump(json_data, f)

with open('hello2.txt', 'r') as f:
    data = json.loads(f.read())

data['data_dict']['element_one'].append("hello4")
#print(data['data_dict']['element_one'])
outputer = ""
for i in data['data_dict']['element_one']:
    outputer = outputer + ", " + i
print(outputer[2:])

with open('hello2.txt', 'w') as f:
    json.dump(data, f)


