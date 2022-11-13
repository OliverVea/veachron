from veachron.application.timing import add_timing_entry, add_timing_exit, list_timings

from veachron.core.timing import TimerTree
from veachron.presentation.api.timings import namespace
from veachron.presentation.api.timings.models import *

from flask import request, jsonify
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
            timestamp=_get_or_none(request.json, 'timestamp'),
            display_name=_get_or_none(request.json, 'displayName'))

        return {'timingId': timing_entry_id}


@namespace.route('/add-exit')
class AddExit(Resource):
    @namespace.expect(add_timing_exit_request_model)
    def post(self):
        add_timing_exit(
            timer_id=request.json['timerId'],
            timing_id=request.json['timingId'],
            timestamp=_get_or_none(request.json, 'timestamp'))

def map_timer_tree(tree: TimerTree, scaling: float):
    return {
        'timerId': tree.timer_id,
        'parentId': tree.parent_id,
        'displayName': tree.display_name,
        'totalTime': tree.total_time,
        'totalPercentage': tree.total_time / scaling,
        'children': [map_timer_tree(child, scaling) for child in tree.children]
    }

@namespace.route('/list-timings')
class ListTimings(Resource):
    #@namespace.marshal_with(list_timers_response_model) Causes CORS problems
    def get(self):
        trees = list_timings()
        scaling = sum(tree.total_time for tree in trees)
        trees = [map_timer_tree(tree, scaling) for tree in trees]
        response = jsonify(*trees)
        response.headers.add('Access-Control-Allow-Origin', '*')
        #print(response.data.decode('utf-8'))
        return response
