

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# //// Note: The following code might not follow the standards, this is purely practice code. The intention of it  //
# //// is to understand concepts and ideas behind testing.                                                          //
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# A programn needs a function that gives us the categorical date, it means that based on the date,
# it should give us if it is night, morning or afteroon time.


# Using Pytest - Unittest, try to make the testing of the following function, remember that it needs
# to be repeteable.

# Check the documentation how to test datetime, it might not be as easy as we might think.
#H int : Use the library freezegun

from datetime import datetime

def get_time_of_day():
    """return string Night/Morning/Afternoon/Evening depending on the hours range"""
    time = datetime.now()
    print("the time", time)
    if 0 <= time.hour <6:
        return "Night"
    if 6 <= time.hour < 12:
        return "Morning"
    if 12 <= time.hour <18:
        return "Afternoon"
    return "Evening"



# Let's assume that a company is saving some information from employees, for this purpose it has built
# a class that has a class which retrieves the information's company, the response is a dictionary that 
# has the following structure {"company" : "zemoga"}. Build a test based on the following class. 

import requests

class Employee:

    def __init__(self, first, last, pay, company):
        self.first = first
        self.last = last
        self.pay = pay
        self.company = company

    def get_company(self):
        url = 'https://company.free.beeceptor.com/company/'
        response = requests.get(f'{url}{self.company}')
        print("response", response.ok)
        if response.ok:
            return response.text
        else:
            return {'response' : 'bad request!'}
        

