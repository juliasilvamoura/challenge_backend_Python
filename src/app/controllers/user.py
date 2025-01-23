from src.app.models.users import User
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from src.app import DB


def init_user_routes(app):
    @app.route("/users/<int:id>", methods=["GET"])
    def get_user_id(id):
        print(id)
        user = User.query.filter_by(id=id).first_or_404()
        print(user)
        return jsonify(user.as_dict()), 200

    @app.route("/users", methods=["POST"])
    def create_user():
        data = request.json

        # Valida se todos os campos obrigatórios estão presentes
        required_fields = ["name", "email", "role_id"]
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"'{field}' is required"}), 400
        
        # Valida se o email já está em uso
        if User.query.filter_by(email=data['email']).first():
            return jsonify({"error": "Email already in use"}), 400

        password = data.get("password", "").strip() or data['email']
        hashed_password = generate_password_hash(password)

        new_user = User(
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            role_id=data['role_id']
        )
        DB.session.add(new_user)
        DB.session.commit()
        return jsonify(new_user.as_dict()), 201