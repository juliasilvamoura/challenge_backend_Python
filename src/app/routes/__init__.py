from flask import request, jsonify
from src.app.controllers.user import get_user, create_user, get_role_by_user, get_role_by_id
from src.app import DB


def routes(app):
    @app.route("/users/<int:id>", methods=["GET"])
    def get_user_id(id):
        user_id = get_user(id)
        if isinstance(user_id, dict) and "error" in user_id:
            return jsonify(user_id), 400  
        if user_id is None: 
            return jsonify({"error": "User not found"}), 404
        return jsonify(user_id.as_dict()), 200
    
    @app.route("/users/role/<int:id>", methods=["GET"])
    def get_role_by_userID(id):
        role = get_role_by_user(id)
        if isinstance(role, dict) and "error" in role:
            return jsonify(role), 400  
        if role is None: 
            return jsonify({"error": "User not found"}), 404
        return jsonify({
            "user_id": role.id,
            "name_user":role.name,
            "role_id": role.role_id
        }), 200
    
    @app.route("/role/<int:role_id>", methods=["GET"])
    def get_role_by_ID(role_id):
        role = get_role_by_id(role_id)
        if isinstance(role, dict) and "error" in role:
            return jsonify(role), 400 
        if role is None: 
            return jsonify({"error": "Role not found"}), 404  
        return jsonify(role.as_dict()), 200  


    @app.route("/users", methods=["POST"])
    def post_user():
        body = request.get_json()
        new_user = create_user(body)
        if isinstance(new_user, dict) and "error" in new_user:
            return jsonify(new_user), 400  
        if new_user is None: 
            return jsonify({"error": "User not found"}), 404
        return jsonify(new_user.as_dict()), 201
    
    @app.route('/')
    def home():
        return jsonify(message="API is working!")