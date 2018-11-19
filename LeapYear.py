

def leapYear():
    year = input('Enter the year : ')
    if len(year) == 4 :
            if int(year)%400 == 0 :
                if int(year) % 100 == 0:
                    if int(year) % 4 == 0:
                         print(year + ' is a leap year')
                    else :
                        print(year + ' is a leap year')
                else:
                    print(year + ' is not a leap year')

            else :
                print(year + ' is a leap year')
    else :
        print( 'Enter proper value : ')
        leapYear()
    return

leapYear()