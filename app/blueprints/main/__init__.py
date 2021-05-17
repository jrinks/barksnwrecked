from flask import Blueprint
from datetime import datetime

bp = Blueprint('main', __name__, url_prefix ='/main')

from . import routes, modelsgit 