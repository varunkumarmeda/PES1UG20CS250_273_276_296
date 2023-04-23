from flask import Flask, render_template, request, flash, redirect, url_for
import requests

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'

def add(n1, n2):
    response = requests.get(f'http://add-service:5051/{n1}/{n2}')
    result = response.json()['result']
    return result

def minus(n1, n2):
    response = requests.get(f'http://minus-service:5052/{n1}/{n2}')
    result = response.json()['result']
    return result

def multiply(n1, n2):
    response = requests.get(f'http://multiply-service:5053/{n1}/{n2}')
    result = response.json()['result']
    return result

def divide(n1, n2):
    response = requests.get(f'http://division-service:5054/{n1}/{n2}')
    result = response.json()['result']
    return result

def gcd(n1, n2):
    response = requests.get(f'http://gcd-service:5055/{n1}/{n2}')
    result = response.json()['result']
    return result

def lcm(n1, n2):
    response = requests.get(f'http://lcm-service:5056/{n1}/{n2}')
    result = response.json()['result']
    return result

def modulus(n1, n2):
    response = requests.get(f'http://modulus-service:5057/{n1}/{n2}')
    result = response.json()['result']
    return result

def greater(n1, n2):
    response = requests.get(f'http://greater-service:5058/{n1}/{n2}')
    result = response.json()['result']
    return result

@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get("first")
    number_2 = request.form.get('second')
    operation = request.form.get('operation')
    result = 0
    try:
            number_1 = int(number_1)
            number_2 = int(number_2)
            if operation == 'add':
                result = add(number_1, number_2)
            elif operation == 'minus':
                result =  minus(number_1, number_2)
            elif operation == 'multiply':
                result = multiply(number_1, number_2)
            elif operation == 'divide':
                result = divide(number_1, number_2)
            elif operation == 'gcd':
                result = gcd(number_1, number_2)
            elif operation == 'lcm':
                result = lcm(number_1, number_2)
            elif operation == 'modulus':
                result = modulus(number_1, number_2)
            elif operation == 'greater than':
                result = greater(number_1, number_2)

            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
    except (TypeError,ValueError,ZeroDivisionError):
            flash("Please enter valid numbers.")

    return render_template('index.html')

if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )