from ast import BoolOp
import random
import logging
from typing import Dict


logging.basicConfig(level=logging.DEBUG)

'''
Random number generator 
Test
test_retrieve_random_number_between_0_and_10
test_retrieve_random_number_between_41_and_50
'''

def retrieve_random_number() -> Dict[str, str]:
    random_int = random.randint(0, 50)
    if random_int>=0 and random_int<=10:
        message = "number between 0 and 10"
    elif random_int>=11 and random_int<=20:
        message = "number between 11 and 20"
    elif random_int>=21 and random_int<=30:
        message = "number between 21 and 30"
    elif random_int>=31 and random_int<=40:
        message = "number between 31 and 40"
    else:
        message = "number between 41 and 50"
    
    return {'message': message, 
            'number' : random_int}

randon_number_gen = retrieve_random_number()
number_generated = randon_number_gen['number']
message_generated = randon_number_gen['message']

logging.debug(f'{message_generated} and the number is {number_generated}')


'''
Save into db example
test_email_not_valid
test_email_valid
test_phone_not_valid
test_phone_valid
test_data_not_valid
test_data_valid
'''
    
import re   
  

  
def check_is_valid_email(email : str) -> Dict[str, bool]:   
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.search(regex,email):   
       message = f'The mail {email} is not valid, please introduce a valid email'
       logging.debug(f'{message}')
       raise Exception(message)

    return {'status' : True}


def check_is_valid_phone_number(phone_number : str) -> Dict[str, bool]:
    
    if not phone_number.isnumeric():   
        message = f'The phone number{phone_number} is not valid, please introduce a valid phone number'
        logging.debug(f'{message}')
        raise Exception(message)
    
    return {'status' : True}
       

def check_if_data_complete(data : str) -> Dict[str, bool]: 
    dictionary_keys = ['name', 'email', 'phone']
    for key in dictionary_keys:    
        if key not in data.keys():
            message = f'The {key} is not present in the object'
            logging.debug(f'{message}')
            raise Exception(message)

    return {'status' : True}
    

def save_db(data : Dict[str, str] , flag_save : bool) -> Dict[str, str]:
    
    msg_data_complete = check_if_data_complete(data)['status']
    msg_valid_email = check_is_valid_email(data['email'])['status']
    msg_valid_phone = check_is_valid_phone_number(data['phone'])['status']
        
    if  not ((msg_data_complete and msg_valid_email and msg_valid_phone) and flag_save):
        return {'message' : 'Data not saved',
                'status' : 'Forbidden'}
    
    return {'message' : 'Data saved',
            'status' : 'OK'}


# data = {'name' : 'Andres F E',
#         'email' : 'andres.echeverri@zemoga.com',
#         'phone' : '57312321123',}


# msg = save_db(data, True)
# print(msg)


# email = "andres.echerri@zemoga.com"  
# message = check_is_valid_email(email)['message']
# logging.debug(f'{message}')   

# email = "andres.echeverri.com"  
# message = check_is_valid_email(email)['message']
# logging.debug(f'{message}')   

# email = "hello-world"  
# message = check_is_valid_email(email)['message']
# logging.debug(f'{message}')   

# phone_number = "57312321123"
# message = check_is_valid_phone_number(phone_number)['message']
# logging.debug(f'{message}')  

# phone_number = "57312321123dsfsf"
# message = check_is_valid_phone_number(phone_number)['message']
# logging.debug(f'{message}')  