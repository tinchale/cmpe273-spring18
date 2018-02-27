from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

students = [
   
]



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Could not find that student with that ID'}), 404)


@app.route('/', methods=['GET'])
def hello():
    return "Hello World!\n"


@app.route('/users', methods=['POST'])
def create_student():
    name = request.form["name"]
    if len(students) == 0:
        newID = 1
    else:
        newID = students[-1]['id'] +1

    student = {
            'id': newID,
            'name': name
        }   
    students.append(student)
    return jsonify(students[-1]), 201


@app.route('/users/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    return jsonify(student[0])


@app.route('/users/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = [student for student in students if student['id'] == student_id]
    if len(student) == 0:
        abort(404)
    students.remove(student[0])
    if len(students) == 0:
        return jsonify(student),204

    return jsonify(student)

