import sys

def upper_or_lower():
    ul = input("Type U for Upper case or L for Lowercase text: ").lower()
    
    if ul == "u":
        ask = input("Enter text which will be outputted in UPPER case: ").upper()
        print (ask)
        sys.exit()
    elif ul == "l": 
        ask = input("Enter text which will be outputted in lower case: ").lower()
        print (ask)
        sys.exit()
    else: 
        print ("Not a valid option.")
        sys.exit()
        
upper_or_lower()
