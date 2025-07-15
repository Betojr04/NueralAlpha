from flask import Blueprint, request, jsonify
from ..services.alpha_service import get_latest_quote
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from ..models.search_history import SearchHistory
from ..models.user import User
from app import db


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


@api.route("/search-history", methods=["POST"])
@jwt_required()
def save_search():
    user_id = get_jwt_identity()
    symbol = request.get_json().get("symbol")

    if not symbol:
        return jsonify({"error": "Symbol is required"}), 400

    search = SearchHistory(user_id=user_id, symbol=symbol.upper())
    db.session.add(search)
    db.session.commit()

    return jsonify({"message": "Search saved"}), 201


@api.route("/search-history", methods=["GET"])
@jwt_required()
def get_search_history():
    user_id = get_jwt_identity()
    history = (
        SearchHistory.query.filter_by(user_id=user_id)
        .order_by(SearchHistory.timestamp.desc())
        .limit(10)
        .all()
    )

    return jsonify(
        [{"symbol": h.symbol, "timestamp": h.timestamp.isoformat()} for h in history]
    )
