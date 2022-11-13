from flask_restx import Namespace

namespace = Namespace('timings', 'Endpoints for managing and viewing timers.')

from veachron.presentation.api.timings.endpoints import *
from veachron.presentation.api.timings.models import *