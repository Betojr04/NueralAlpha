from flask import Blueprint, request, jsonify
from ..services.alpha_service import get_latest_quote
from flask_jwt_extended import jwt_required, get_jwt_identity


api = Blueprint("api", __name__)


@api.route("/quote")
def quote():
    symbol = request.args.get("symbol")
    if not symbol:
        return jsonify({"error": "Missing 'symbol' query parameter"}), 400

    try:
        data = get_latest_quote(symbol.upper())
        quote = data.get("Global Quote", {})

        if not quote:
            return jsonify({"error": "Not a valid symbol, please try again."}), 404

        # Optional: return simplified result
        simplified = {
            "symbol": quote.get("01. symbol"),
            "price": quote.get("05. price"),
            "volume": quote.get("06. volume"),
            "previous_close": quote.get("08. previous close"),
            "change_percent": quote.get("10. change percent"),
        }

        return jsonify(simplified)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@api.route("/dashboard-data", methods=["GET"])
@jwt_required()
def dashboard_data():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"email": user.email})
