def canDivideNoRem(dividend,divisor):

    if(dividend%divisor==0):
        return True
    else:
        return False

def main():
    dividend=44
    divisor=4
    returnValue=canDivideNoRem(dividend, divisor)

    print( 'canDivideNoRem(',dividend,',',divisor,') returned', returnValue)
    dividend=20
    divisor=3
    returnValue=canDivideNoRem(dividend, divisor)
    print( 'canDivideNoRem(',dividend,',',divisor,') returned', returnValue)

if __name__ == '__main__':
    main()
