"""
This is simple example of how to receive a webhook event from nautobot
"""
from fastapi import APIRouter, Depends
from app.dependencies import get_x_hook_signature_header
from app.models.nautobot import Event, EventRoot

router = APIRouter(
    prefix='/webhook',
    dependencies=[Depends(get_x_hook_signature_header)],
    tags=['webhook'],
    responses={404: {'description': 'Not Found'}}
)


@router.post('/device')
async def post_device_message(event: EventRoot):
    print(f"event: {event}")
    # do something with the `event`
    return "ok"
