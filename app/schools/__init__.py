from flask import Blueprint

school_spider = Blueprint('school_spider', __name__)

from . import school, errors