# myapp/utils.py
from twilio.rest import Client
from django.conf import settings

def send_sms(to_number, body_text):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        from_=settings.TWILIO_PHONE_NUMBER,
        body=body_text,
        to=to_number
    )
    return message.sid
