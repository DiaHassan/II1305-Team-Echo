from os import path as os_path
from sys import path as sys_path
sys_path.append(os_path.dirname(os_path.dirname(__file__)))
# Import flask
from flask import Flask, jsonify, request
from flask_cors import CORS


# Import extract
try:
  from db.extract import extract
except ImportError:
  from .db.extract import extract

from code.webscrape import runWebscrape





# import commit

# App
app = Flask(__name__)
CORS(app)
@app.route('/why', methods=['GET','POST'])

# Extracts data for json request
def endpoint():
    data = request.get_json()
    arg1 = data['job']
    print("Arg1: ", arg1)
    if(arg1[3]=='Inget val'):
        arg1[3] = 'null'
    info = extract(arg1[0],arg1[1],arg1[2],arg1[3],arg1[4])
    print(info)
    return jsonify({'number':(info)})

@app.route('/test', methods=['GET','POST'])

def runOAM():

    print(1)
    
    runWebscrape()
    return jsonify({'number':(2)})

# Main function
def run():
    app.run(host="0.0.0.0",debug=False, port=8888)


# Run main function
if __name__ == '__main__':
    run()