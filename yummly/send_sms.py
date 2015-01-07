# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

from secret import sid, token

client = TwilioRestClient(sid, token)

message = client.messages.create(
    to="+19413200462",
    from_="+19419607434",
    body="Hello there!",
    media_url=[
        'https://demo.twilio.com/owl.png',
        'https://demo.twilio.com/logo.png'
    ]
)
