from flask import Flask, jsonify,request
# , jsonify, request
from flask_cors import CORS
from extract import extract

# def my_function(arg1, arg2):
#     # do something with arg1 and arg2
#     result = arg1 + arg2
#     return result



app = Flask(__name__)
CORS(app)

@app.route('/why', methods=['GET','POST'])
def endpoint():

    data = request.get_json()
    arg1 = data['job']
    print(arg1)
    info = extract(arg1[0],arg1[1],arg1[2],arg1[3])
    # info.pop(0)
    print(info)

    return jsonify({'number':(info)})



app.run(port=8888)