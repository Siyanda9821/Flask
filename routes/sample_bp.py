from pprint import pprint

from flask import Blueprint, render_template, request

HTTP_NOT_FOUND = 404
sample_bp = Blueprint("sample_bp", __name__)


@sample_bp.get("/")
def sample_bp_page():
    return render_template(
        "sample_bp.html",
    )
