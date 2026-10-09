from flask import Flask, jsonify, request


app = Flask(__name__)

students = [
    {
        "id": 1,
        "name": "Ali Hassan",
        "major": "Computer Engineering",
    },
    {
        "id": 2,
        "name": "Sara Ahmad",
        "major": "Software Engineering",
    },
    {
        "id": 3,
        "name": "Omar Khaled",
        "major": "Computer Science",
    },
    {
        "id": 4,
        "name": "Lina Mahmoud",
        "major": "Information Systems",
    },
    {
        "id": 5,
        "name": "David Johnson",
        "major": "Cybersecurity",
    },
]


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Student REST API"}), 200


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students), 200


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return jsonify(student), 200

    return jsonify({"error": "Student not found"}), 404


@app.route("/students", methods=["POST"])
def add_student():
    data = request.get_json(silent=True)

    if not data or "name" not in data or "major" not in data:
        return jsonify({"error": "Name and major are required"}), 400

    new_id = max(student["id"] for student in students) + 1
    new_student = {
        "id": new_id,
        "name": data["name"],
        "major": data["major"],
    }
    students.append(new_student)

    return jsonify(new_student), 201


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return jsonify(
                {
                    "message": "Student deleted successfully",
                    "student": student,
                }
            ), 200

    return jsonify({"error": "Student not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
