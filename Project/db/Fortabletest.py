from flask import Flask, jsonify,request
# , jsonify, request
from flask_cors import CORS
from extract import get_profession_in_counties, get_professions_in_county

# def my_function(arg1, arg2):
#     # do something with arg1 and arg2
#     result = arg1 + arg2
#     return result


app = Flask(__name__)
CORS(app)

@app.route('/why', methods=['GET','POST'])
def endpoint():

    data = request.get_json()
    arg1 = data['nb']
    return jsonify({'number':str(get_profession_in_counties('Städare'))})



app.run()