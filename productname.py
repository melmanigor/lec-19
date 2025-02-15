import re
product_name="kkjkjkk"
def check_product_name(product_name):
    x=re.findall("^[0-9A-Za-z]{2,50}$",product_name)
    if x==[]:
        return False
    else:
        return True
#x=re.findall("^[\w]{2,50}$",product_name)
