from application.timing import add_timing_entry, add_timing_exit, list_timings

from presentation.api.timings import namespace
from presentation.api.timings.models import *

from flask import request
from flask_restx import Resource

def _get_or_none(source, key: str):
    return source[key] if key in source else None

@namespace.route('/add-entry')
class AddEntry(Resource):
    @namespace.expect(add_timing_entry_request_model)
    @namespace.marshal_with(add_timing_entry_response_model)
    def post(self):
        timing_entry_id = add_timing_entry(
            timer_id=request.json['timerId'],
            timer_parent_id=_get_or_none(request.json, 'timerParentId'),
            timing_id=_get_or_none(request.json, 'timingId'),
            timestamp=_get_or_none(request.json, 'timestamp'))

        return {'timingId': timing_entry_id}


@namespace.route('/add-exit')
class AddExit(Resource):
    @namespace.expect(add_timing_exit_request_model)
    def post(self):
        add_timing_exit(
            timer_id=request.json['timerId'],
            timing_id=request.json['timingId'],
            timestamp=_get_or_none(request.json, 'timestamp'))


@namespace.route('/list_timings')
class ListTimings(Resource):
    def get(self):
        return list_timings("A")
