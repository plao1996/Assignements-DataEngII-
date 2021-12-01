import numpy as np
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello() :
    return "Welcome to my app"

@app.route('/mean', methods=['GET'])
def mean():
        to_list = request.args.get("list")
        if(to_list is None):
            return "no list given"
        list_split = to_list.split(",")
        numbers = list(map(int,list_split))
        total = np.mean(numbers)
        return "{}".format(total)

if __name__ == '__main__':
    app.run(debug=True)