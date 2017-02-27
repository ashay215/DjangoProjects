from twilio.rest import TwilioRestClient

# put your own credentials here
ACCOUNT_SID = "AC689b9870c4d29eba070ffccd0b133bf6"
AUTH_TOKEN = "0688615be0d3415f952e6cb8ea0148f8"

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

client.messages.create(
    to="2135958747",
    from_="2139081961",
    body="This is the ship that made the Kessel Run in fourteen parsecs?",
)
