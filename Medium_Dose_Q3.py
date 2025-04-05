
# medium dose: Q3
# Assuming that if the shifted characters are lesser than A, then we start shifting furthur up from Z.

def decode(code):

    code = code.upper()   # converting input to upper case

    message = ""     # Output variable

    for i in range(0,len(code)):
        if ord(code[i])-i-1 >= ord("A"):
            message += chr(ord(code[i])-i-1)
        else:
            message += chr( ord("Z") - ( i - (ord(code[i])-ord("A")) ))   # if shifted char go below A, shift furthur up form Z
            
    return message
  
print(decode("ALRight"))