from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Modulus(Resource):
    def get(self, num1, num2):
        result = num1 % num2
        return {'result': result}


api.add_resource(Modulus, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5057)
