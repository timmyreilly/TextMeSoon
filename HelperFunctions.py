from tokens import *
from tokens import *
from HelperFunctions import *
from azure.storage import QueueService

ACCOUNT_SID = get_account_sid()
AUTH_TOKEN = get_auth_token()
TWILIO_NUMBER = get_twilio_number()
MY_PHONE_NUMBER = get_phone_number()



def get_working_queue():
    return WORKING_QUEUE

def get_storage_account_name():
    return STORAGE_ACCOUNT

def get_storage_account_key():
    return STORAGE_KEY

def get_account_sid():
	return ACCOUNT_SID
	
def get_auth_token():
	return AUTH_TOKEN

def get_twilio_number():
    return TWILIO_SANDBOX_NUMBER

def get_phone_number():
    return MY_PHONE_NUMBER
    
account_name = get_storage_account_name()
account_key = get_storage_account_key()
working_queue = get_working_queue()

queue_service = QueueService(account_name, account_key)

def get_state_managed_queue():
        messages = queue_service.get_messages(working_queue)
    for message in messages:
        print(message.message_text)
        queue_service.delete_message(working_queue, message.message_id, message.pop_receipt)
    return str(message.message_text)