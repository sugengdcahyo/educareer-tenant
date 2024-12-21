from . import mongo
from bson.objectid import ObjectId

def get_students():
    """Fetch all students from the database."""
    students = mongo.db.students.find()
    return [student for student in students]

def add_student(data):
    """Add a new student to the database."""
    print(data)
    student = {
        'student_id': data['student_id'],
        'name': data['name'],
        'major': data.get('major', ''),
        'email': data.get('email', ''),
        'gpa': data.get('gpa', 0.0),
    }
    mongo.db.students.insert_one(student)

def delete_student(student_id):
    """Delete a student by ID."""
    mongo.db.students.delete_one({'_id': ObjectId(student_id)})

def update_student(student_id, data):
    """Update student details."""
    update_data = {key: value for key, value in data.items() if value}
    mongo.db.students.update_one(
        {'_id': ObjectId(student_id)},
       {'$set': update_data}
    )

