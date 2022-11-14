from veachron.presentation.api.timings import namespace
from flask_restx import fields

add_timing_entry_request_model = namespace.model('AddTimingEntry', {
    'timerParentId': fields.String(required=False, description='Identifier used to identify code segment in overview.'),
    'timingId': fields.String(required=False, description='Used to match the entry with an exit. If not set, a randomly generated one will be returned.'),
    'timestamp': fields.Float(required=False, description='Timestamp of the entry.'),
    'displayName': fields.String(required=False, description='The display name of the timer. The display name provided the latest is used.')
})

add_timing_entry_response_model = namespace.model('AddTimingEntryResponse', {
    'timingId': fields.String(description='Used to match the entry with an exit. If not set, a randomly generated one will be returned.')
})

add_timing_exit_request_model = namespace.model('AddTimingExit', {
    'timestamp': fields.Float(required=True, description='Timestamp of the exit.')
})

list_timers_response_model = namespace.model('ListTimersResponse', {
    'timerId': fields.String(),
    'parentId': fields.String(required=False),
    'displayName': fields.String(),
    'totalTime': fields.Float(),
    'totalPercentage': fields.Float()
})

list_timers_response_model['children'] = fields.List(fields.Nested(list_timers_response_model), default=[])
