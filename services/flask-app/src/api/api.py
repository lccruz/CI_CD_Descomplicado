from flask import Blueprint

api_bp = Blueprint('api', __name__)


@api_bp.route('/', methods=["GET"])
def home() -> dict:
    """Home."""
    return {
        "data": "Welcome to API Home Page!"
    }


@api_bp.route('/about', methods=["GET"])
def about() -> str:
    """About."""
    return "This is the About Page."
