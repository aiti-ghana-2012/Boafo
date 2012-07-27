import urls
import models

def sample_sms_handler(sms):
    print sms.to_message()

def sms_request(sms):
    dest = sms.to_number
    customer = sms.from_number
    new_sms = sms(to_number=customer, from_number=dest, body="Hello, please type something in here")
    new_sms.send()
