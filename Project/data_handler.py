# Import flask
from flask import Flask, jsonify, request
from flask_cors import CORS

# Import extract
try:
  from db.extract import extract, delete_rows
except ImportError:
  from .db.extract import extract, delete_rows

from code.webscrape import runWebscrape
# try:
#   from code.webscrape import runWebscrape
# except ImportError:
#   from .code.webscrape import runWebscrape


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
    # print(1)
    picker = request.get_json()
    print(picker['test'])
    runWebscrape(picker['test'])
    return jsonify({'number':(2)})


@app.route('/rd', methods=['GET','POST'])

def removeDate():
   print("removing date")
   date = request.get_json()
   print(date['test'])
   delete_rows(date['test'])
   return jsonify({'number':(2)})
   # Function name

@app.route('/sd', methods=['GET','POST'])

def saveDb():
   print("Save DB")
   # Function name
   return jsonify({'number':(2)})


# Main function
def run():
    app.run(host="0.0.0.0",debug=False, port=8888)


# Run main function
if __name__ == '__main__':
    run()