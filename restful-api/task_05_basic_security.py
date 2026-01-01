#!/usr/bin/python3
"""
Task 05: API Security and Authentication Techniques
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# In-memory users storage
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# -------------------------
# Basic Authentication
# -------------------------
@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if not user:
        return None
    if check_password_hash(user["password"], password):
        return user
    return None


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# -------------------------
# JWT Authentication
# -------------------------
@app.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 401

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_access_token(identity=user)
    return jsonify({"access_token": token})


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    user = get_jwt_identity()
    if user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


# -------------------------
# JWT Error Handlers (VERY IMPORTANT)
# -------------------------
@jwt.unauthorized_loader
def unauthorized_callback(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(err):
    return jsonify({"error": "Invalid token"}), 401
