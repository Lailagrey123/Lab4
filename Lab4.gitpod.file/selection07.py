def zipZapZop():
    number=int(input("Enter a number: "))
    if(number%3==0):
        print("zip",end="")
    if(number%5==0):
        print("zap",end="")
    if(number%7==0):
        print("zop",end="")
    if(number%3!=0 and number%5!=0 and number%7!=0):
        print(number)


zipZapZop
