from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC8a162ff5c2ce6bb45fbd77427bd8e8d6'
auth_token = 'fddc43cf2e8a8fa8d2107eeca58fbdae'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+12029027692',
                              body='Person is detected !!!!',
                              to='+919146546533'
                          )

print(message.sid)