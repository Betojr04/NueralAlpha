from flask import Blueprint, request, jsonify
from services.alpha_service import get_latest_quote

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
