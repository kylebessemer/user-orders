from . import blueprint
from flask import request, jsonify
from ...services.users import lookup

@blueprint.route('/lookup/<int:id>', methods=['GET'])
def users_lookup(id):
    user = lookup(id)

    if user:
        return jsonify({
            "success": True,
            "message": "User found",
            "user": user.to_json
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the user"
        }), 404
