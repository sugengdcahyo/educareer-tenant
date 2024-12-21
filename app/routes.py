from flask import Blueprint, render_template, request, jsonify 
from .models import get_students, add_student, update_student, delete_student
from . import mongo


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    students = get_students()
    return render_template('index.html', students=students)


@main_bp.route('/health', methods=['GET'])
def health_check():
    try:
        # Coba akses koleksi MongoDB
        mongo.db.list_collection_names()
        return jsonify({'status': 'success', 'message': 'MongoDB is connected'}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500


@main_bp.route('/students', methods=["POST"])
def add_student_route():
    data = request.json
    if not data.get("name") or not data.get("student_id"):
        return jsonify({
            "error": "Missing required fields."
        }), 400
    add_student(data)
    return jsonify({"message": "Student added successfully"}), 201


@main_bp.route('/students/<student_id>', methods=['GET', 'PUT', 'DELETE'])
def students_route(student_id):
    if request.method == 'GET':
        students = get_student_by_id(student_id)
    elif request.method == 'PUT':
        data = request.json
        update_student(student_id, data)
        return jsonify({"message": "Updated student successfully"}), 200
    elif request.method == 'DELETE':
        delete_student(student_id)
        return jsonify({"message": "Deleted student successfully"}), 200


@main_bp.route('/students/<student_id>', methods=['PUT'])
def update_student_route(student_id):
    data = request.json
    update_student(student_id, data)
    return jsonify({'message': 'Student updated successfully'}), 200
