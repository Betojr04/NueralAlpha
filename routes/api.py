from flask import Blueprint, jsonify
from services.alpaca_service import fetch_latest_quote, analyze_stock

api_bp = Blueprint("api", __name__)


@api_bp.route("/quote/<symbol>")
def get_quote(symbol):
    return jsonify(fetch_latest_quote(symbol))


@api_bp.route("/analyze/<symbol>")
def analyze(symbol):
    return jsonify(analyze_stock(symbol))
