from . import blueprint
from flask import jsonify
from ...services.orders import lookup

@blueprint.route('/lookup/<int:id>', methods=['GET'])
def orders_lookup(id):
    order = lookup(id)

    if order:
        return jsonify({
            "success": True,
            "message": "Order found",
            "order": order.to_json
        }), 200
    else:
        return jsonify({
            "success": False,
            "message": "Failed to find the order"
        }), 404