import json
import functools
def to_json(func):
    @functools.wraps(func)
    def parser(*args, **kwargs):
        result = func(*args, **kwargs)
        #from io import StringIO
        #io = StringIO()
        #json.dump(result,io)
        store = json.dumps(result)
        #outputer = json.loads(store)
        print(store)
        return store
    return parser

@to_json
def get_data():
    return {
            'data': 42
        }

#print(get_data.__name__)
print(get_data())


