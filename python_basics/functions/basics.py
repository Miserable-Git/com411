# Using a user defined function to return a built in function
def ordandhex (char):
    ordi = str(ord(char))
    ordihex = str(hex(ord(char)))
    rtn = str(ordi +" "+ ordihex)

    return rtn



while True:
    print("Input a character to retrieve its ASCII and HEX code")
    print(ordandhex(input()))


