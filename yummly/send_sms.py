# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

from secret import sid, token

# Find these values at https://twilio.com/user/account
account_sid = account_sid
auth_token = auth_token
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+19413200462", from_="+19419607434",
                                     body="Hello there!",
                                     media_url=['https://demo.twilio.com/owl.png', 'https://demo.twilio.com/logo.png'])