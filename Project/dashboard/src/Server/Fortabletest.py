from flask import Flask, jsonify,request
# , jsonify, request
from flask_cors import CORS

def my_function(arg1, arg2):
    # do something with arg1 and arg2
    result = arg1 + arg2
    return result


app = Flask(__name__)
CORS(app)

@app.route('/why', methods=['GET','POST'])
def endpoint():
    # return 
    data = request.get_json()
    arg1 = data['nb']
    # arg2 = data['arg2']
    result = my_function(arg1, 8)
    return jsonify({'number':str(result)})



app.run()