def isOdd(argument):
    if(argument%2!=0):
        return True
    else:
        return False
        #lab4edit
    
    
def main():
    argument = 5
    returnValue = isOdd( argument )
    print( 'isOdd(',argument,') returned', returnValue)

    argument = 10
    returnValue = isOdd( argument )
    print( 'isOdd(',argument,') returned', returnValue)

if __name__ == '__main__':
    main()
