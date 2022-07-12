import pytest

from unittest.mock import patch
from unittest import mock
from course.src.user_example import retrieve_random_number, check_is_valid_phone_number, check_is_valid_email, check_if_data_complete, save_db
import random

'''
user_example 
'''


@patch("random.randint")
def test_retrieve_random_number_between_0_and_10(mock_random : mock) -> None:
    mock_random.return_value = 5
    
    randon_number_gen = retrieve_random_number()
    assert randon_number_gen['number'] == 5
    assert randon_number_gen['message'] == 'number between 0 and 10'
  

@patch("random.randint")
def test_retrieve_random_number_between_41_and_50(mock_random : mock) -> None:
    mock_random.return_value = 45
    
    randon_number_gen = retrieve_random_number()
    assert randon_number_gen['number'] == 45
    assert randon_number_gen['message'] == 'number between 41 and 50'
  
  
    
'''
save_db
'''
mock_data_sucess = {'name' : 'mock_name',
                    'email' : 'mock@mock.com',
                    'phone' : '0000000000',}

mock_data_invalid = {'name' : 'mock_name',
                    'email' : 'mock.mock.com',
                    'phone' : '+5700000',}

mock_dict_invalid = {'name' : 'mock_name',
                    'mail' : 'mock.mock.com',
                    'phone' : '+0000000000',}
    
@patch("course.src.user_example.save_db")
def test_email_not_valid(mock_save_db : mock) -> None:
    with pytest.raises(Exception) as excinfo:
        check_is_valid_email(mock_data_invalid['email'])
    assert excinfo.value.args[0] == f'The mail {mock_data_invalid["email"]} is not valid, please introduce a valid email'
    
@patch("course.src.user_example.save_db")
def test_email_valid(mock_save_db : mock) -> None:
    msg_valid_email = check_is_valid_email(mock_data_sucess['email'])['status']
    assert msg_valid_email == True
    
@patch("course.src.user_example.save_db")
def test_phone_not_valid(mock_save_db : mock) -> None:
    with pytest.raises(Exception) as excinfo:
        check_is_valid_phone_number(mock_data_invalid['phone'])
    assert excinfo.value.args[0] == f'The phone number{mock_data_invalid["phone"]} is not valid, please introduce a valid phone number'

@patch("course.src.user_example.save_db")
def test_phone_valid(mock_save_db : mock) -> None:
    msg_phone_email = check_is_valid_phone_number(mock_data_sucess['phone'])['status']
    assert msg_phone_email == True
    
@patch("course.src.user_example.save_db")
def test_data_not_valid(mock_save_db : mock) -> None:
    with pytest.raises(Exception) as excinfo:
        check_if_data_complete(mock_dict_invalid)
    assert excinfo.value.args[0] == f'The email is not present in the object'
    
@patch("course.src.user_example.save_db")
def test_data_valid(mock_save_db : mock) -> None:
    msg_data = check_if_data_complete(mock_data_sucess)['status']
    assert msg_data == True
    
@patch("course.src.user_example.check_is_valid_email")
@patch("course.src.user_example.check_is_valid_phone_number")
@patch("course.src.user_example.check_if_data_complete")
def test_save_db_success(mock_check_if_data_complete : mock, 
                        mock_check_is_valid_phone_number: mock, 
                        mock_check_is_valid_email : mock) -> None:
    mock_check_if_data_complete.return_value = {'status' : True}
    mock_check_is_valid_phone_number.return_value = {'status' : True}
    mock_check_is_valid_email.return_value = {'status' : True}
    msg = save_db(mock_data_sucess, True)
    assert msg['message'] == 'Data saved'
    assert msg['status'] == 'OK'
    
    
@patch("course.src.user_example.check_is_valid_email")
@patch("course.src.user_example.check_is_valid_phone_number")
@patch("course.src.user_example.check_if_data_complete")
def test_save_db_failure(mock_check_if_data_complete : mock, 
                         mock_check_is_valid_phone_number : mock, 
                         mock_check_is_valid_email : mock) -> None:
    mock_check_if_data_complete.return_value = {'status' : True}
    mock_check_is_valid_phone_number.return_value = {'status' : True}
    mock_check_is_valid_email.return_value = {'status' : True}
    msg = save_db(mock_data_sucess, False)
    assert msg['message'] == 'Data not saved'
    assert msg['status'] == 'Forbidden'