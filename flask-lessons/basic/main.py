from flask import Flask, request
# from datetime import datetime

app = Flask(__name__)



@app.route('/')
def index():
    return '<h3>Hello, World!</h3>'

@app.route('/spam')
def spam():
    person = {'name': 'John', 'age': 21 }
    return person

@app.route('/hello/<name>')
def hello(name):
    # name = request.args.get('name')
    # name = 'Jack'
    return {'message': f'Hello, {name}'}

# @app.route('/add/<int:num1>/<int:num2>')
# def add(num1, num2):
#         # num1 = int(request.args.get('num1'))
#         # num2 = int(request.args.get('num2'))
#         return {'result': num1 + num2}

# @app.route('/current_time')
# def current_time():
#     time = datetime.now()
#     timestamp = time.strftime("%H:%M")
#     return f'<p>{timestamp}</p>'

@app.errorhandler(TypeError)
def type_error(error):
    return {'error': str(error)}, 400

@app.errorhandler(404)
def not_found(error):
    return {'error': str(error)}, 404

@app.route("/calculator/<int:num1>/add/<int:num2>")
def add(num1, num2):
    answer = {"operation": str(num1) + " plus " + str(num2),
    "result": num1 + num2}
    return answer

@app.route("/calculator/<int:num1>/subtract/<int:num2>")
def subtract(num1, num2):
    return {"operation": str(num1) +" minus "+ str(num2),
    "result": num1 - num2}

@app.route("/calculator/<int:num1>/divide/<int:num2>")
def divide(num1, num2):
    return {"operation": str(num1) + " divided " + str(num2),
    "result": num1 / num2}

@app.route("/calculator/<int:num1>/multiply/<int:num2>")
def multiply(num1, num2):
    return {"operation": str(num1) + " multiplied " + str(num2),
    "result": num1 * num2}


if __name__ == '__main__':
    app.run(debug=True)