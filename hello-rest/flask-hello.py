from flask.ext.api import FlaskAPI
from flask import request, url_for

app = FlaskAPI(__name__)

def get_numbers_from_request(req):
   num_1, num_2 = request.data.get('num_1'), request.data.get('num_2')
   return int(num_1), int(num_2)

def prep_output(operation, val):
   return {
      operation: val
   }

@app.route("/add", methods=['POST'])
def add():
   num_1, num_2 = get_numbers_from_request(request)
   sum = num_1 + num_2
   return prep_output('sum', sum)

@app.route("/sub", methods=['POST'])
def sub():
   num_1, num_2 = get_numbers_from_request(request)
   diff = num_1 - num_2
   return prep_output('diff', diff)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
