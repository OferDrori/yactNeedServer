from flask import Flask, request, jsonify
from markupsafe import escape

from recommender import aiFunc

app = Flask(__name__)
@app.route('/api' ,methods=['POST'])
def api_ai():
    req_data = request.get_json()
    age = req_data['age']
    yearsOfExperience = req_data['years of experience']
    numberOfChildren = req_data['how many children']
    example = req_data['location']
    sex = req_data['sex']
    return aiFunc(age,yearsOfExperience,numberOfChildren,sex)



@app.route('/')
def hello_b():
    return 'fadad'
if __name__ == '__main__':
    app.run()