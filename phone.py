import re




def check_phone(phone):
    x=re.findall("^[0-9]{3}[-][0-9]{2}[-][0-9]{7}$",phone)
    if x==[]:
        return False
    else:
        return True

   
phone="972-52-1234567" 


