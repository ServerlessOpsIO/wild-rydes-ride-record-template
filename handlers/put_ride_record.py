'''Put ride record'''

import json
import logging
import os

import boto3

log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))  # type: ignore
_logger = logging.getLogger(__name__)

# FIXME: DynamoDB
# - Get table name from environment
# - Create DynamoDB resource object
# - Create DynamoDB Table object

def _get_body_from_event(event):
    '''Get data from event body'''
    # FIXME: Return the body of the API Gateway request contained in the
    # trigger event.
    #
    # HINT: see tests/events/put_ride_record.json
    pass


def _put_ride_record(ride_record):
    '''Put record item into DynamoDB table.'''
    # FIXME: Take the ride_record and insert it into DynamoDB
    pass


def handler(event, context):
    '''Function entry'''
    _logger.debug('Event received: {}'.format(json.dumps(event)))

    ride_record = _get_body_from_event(event)
    _put_ride_record(ride_record)

    resp = {
        'statusCode': 201,
        'body': json.dumps({'success': True})
    }
    _logger.debug('Response: {}'.format(json.dumps(resp)))
    return resp

