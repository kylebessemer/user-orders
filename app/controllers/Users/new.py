from . import blueprint
from flask import request, jsonify
from ...services.users import new

@blueprint.route('/new', methods=['POST'])
def users_new():
    body = request.get_json()

    first_name = body["first_name"]
    last_name = body["last_name"]

    new_user = new(first_name, last_name)

    if new_user:
        return jsonify({
            "success": True,
            "message": "User added successfully",
            "user": new_user.to_json
        }), 201
    else:
        return jsonify({
            "success": False,
            "message": "Failed to add the user"
        }), 500
