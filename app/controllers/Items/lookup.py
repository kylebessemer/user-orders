from . import blueprint
from flask import request, jsonify
from ...services.items import lookup

@blueprint.route('/lookup/<int:id>', methods=['GET'])
def items_lookup(id):
    body = request.get_json()

    page = body["page"]
    page_size = body["page_size"]

    query = lookup(id, page, page_size)

    if query["item"]:
        return jsonify({
            "success": True,
            "message": "Item found",
            "item": query["item"].to_json,
            "pagination": query["pagination"]
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the item"
        }), 404
