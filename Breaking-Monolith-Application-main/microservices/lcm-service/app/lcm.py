from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Lcm(Resource):
    def get(self, num1, num2):
        if num1 == 0 or num2 == 0:
            return {'result': 0}
        else:
            max_num = max(num1, num2)
            while True:
                if max_num % num1 == 0 and max_num % num2 == 0:
                    return {'result': max_num}
                max_num += 1


api.add_resource(Lcm, '/<int:num1>/<int:num2>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5056)
