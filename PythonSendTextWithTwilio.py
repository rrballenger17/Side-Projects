from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "ACea838335e059e27d9201c68fd51b9396"
auth_token  = "{insert token # here}"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="Wake up Neo...\n The Matrix has you... \n Follow the white rabbit \n",
    to="+16144064942",    # Replace with your phone number
    from_="+16502295732") # Replace with your Twilio number
print message.sid
