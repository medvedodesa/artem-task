from flask import Blueprint

bp = Blueprint('mach', __name__)

from app.mach import routes