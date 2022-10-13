from flask import Blueprint
from flask_restx import Api
blueprint = Blueprint('api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='Veacron Swagger',
    version='0.0.1a',
    description='API for the timing application veachron.',
    doc='/swagger'
)

from veachron.presentation.api.timings import namespace as timings
api_extension.add_namespace(timings)
