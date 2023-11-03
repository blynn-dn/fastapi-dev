"""
This is simple example of how to receive a webhook event from nautobot
"""
import logging

from fastapi import APIRouter, Depends
from app.dependencies import get_x_hook_signature_header
from app.models.nautobot import Event, EventRoot

logger = logging.getLogger(__name__)

# create /webhook API router endpoint
router = APIRouter(
    prefix='/webhook',
    dependencies=[Depends(get_x_hook_signature_header)],
    tags=['webhook'],
    responses={404: {'description': 'Not Found'}}
)


@router.post('/device')
async def post_device_message(event: EventRoot):
    """simple nautobot webhook event receiver"""

    # log the event
    logger.info(f"event: {event}")

    """
    Do something with the `event`.  Typical use case is to perform asynchronous processing.  For example:
        * publish to a queue, topic for additional processing
        * publish the event as a Celery task
        * persist the vent to a db 
        * send a notification message such as to Slack, SNS, Lambda function, etc.
    """
    return "ok"
