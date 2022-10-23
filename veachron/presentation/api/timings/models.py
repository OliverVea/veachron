from veachron.presentation.api.timings import namespace
from flask_restx import fields

add_timing_entry_request_model = namespace.model('AddTimingEntry', {
    'timerId': fields.String(required=True, description='Identifier used to identify code segment in overview.'),
    'timerParentId': fields.String(required=False, description='Identifier used to identify code segment in overview.'),
    'timingId': fields.String(required=False, description='Used to match the entry with an exit. If not set, a randomly generated one will be returned.'),
    'timestamp': fields.Integer(required=False, description='Timestamp of the entry.'),
    'displayName': fields.String(required=False, description='The display name of the timer. The display name provided the latest is used.')
})

add_timing_entry_response_model = namespace.model('AddTimingEntryResponse', {
    'timingId': fields.String(required=False, description='Used to match the entry with an exit. If not set, a randomly generated one will be returned.')
})

add_timing_exit_request_model = namespace.model('AddTimingExit', {
    'timerId': fields.String(required=True, description=''),
    'timingId': fields.String(required=True, description='Used to match the exit with an entry.'),
    'timestamp': fields.Integer(required=True, description='Timestamp of the exit.')
})
