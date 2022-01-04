from flask import Flask, jsonify
from flask import request


todos = [
    { "label": "Walk dog", "done": False }
]

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    json_todos = jsonify(todos)
    return json_todos, 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    return jsonify(todos), 201 




# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)