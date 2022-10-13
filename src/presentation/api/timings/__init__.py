from flask_restx import Namespace
namespace = Namespace('Timings', 'Endpoints for managing and viewing timers.')

from presentation.api.timings.models import *
from presentation.api.timings.endpoints import *
