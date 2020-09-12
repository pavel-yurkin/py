import json
import os
import tempfile
import argparse
import sys

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
filesize = 0
try:
    filesize = os.path.getsize(storage_path)
except Exception:
    with open(storage_path, 'w') as f:
        f.write("")
if filesize != 0:
    with open(storage_path, "r") as f:
        data = json.loads(f.read())
else:
    data = dict()

parser = argparse.ArgumentParser()
parser.add_argument("--key", help = "this is key", action = "store_true")
parser.add_argument("--val", help = "this is val", action = "store_true")

parser.add_argument("value_of_key", type = str, help = "this is key value")

if len(sys.argv) < 4:
    args = parser.parse_args()
    
    if args.value_of_key not in data.keys() or filesize == 0:
        print(None)
    else:
        outputer = ""
        for i in data[args.value_of_key]:
            outputer = outputer + ", " + i
        print(outputer[2:])
else:
    parser.add_argument("value_of_val", type = str, help = "this is val value")
    args = parser.parse_args()

    if args.value_of_key not in data.keys():
        data[args.value_of_key] = list()
        data[args.value_of_key].append(args.value_of_val)
    else:
        data[args.value_of_key].append(args.value_of_val)

    with open(storage_path, 'w') as f:
        json.dump(data, f)

