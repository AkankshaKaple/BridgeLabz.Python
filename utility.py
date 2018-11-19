import random
from time import time


class utility:
    def __init__(self):
        pass
 ########################################################################################
    def Fact(self, input):
            fact = 1
            for i in range(1,self.input+1):
                fact = i * fact
            return fact
#########################################################################################
    #his program prints the number of times a person won and percentage
    # of win and loss
    def GambleingMethod(self,numberOfBets, goal, money):
        win = 0
        lose = 0
        count =0

        for i in range(numberOfBets):
            randomNumber = random.random() #Generate random numbers between 0 to 1
           # print(randomNumber)
            count+=1   #Number of times the namdom number is generating
            if randomNumber > 0.5:  # Win
                money += 1
                win += 1
               # print(self.money)
            else:                   # Lose
                money -= 1
                lose += 1
               # print(self.money)

            if money == goal:
                print('You have reached your goal on bet number ' + str(count))
                break
            elif money == 0:
                print('You have exhausted your money')
                break
        print('Number of win : ' + str(win))
        print('Number of lose :' + str(lose))
        print('Percentage of win : ' + str((win*100)/count))
        print('Percentage of lose : ' + str((lose*100)/count))

#########################################################################################
    # This program shows the harmonic values till number N given by user
    def HarmonicValue(self, number):
        result = 0
        for i in range(1, number + 1):
            result = result + (1 / i)
        return result

#########################################################################################
# This program returns whether the given year is leap year or not
    def leapYear(self, year):

        if len(year) == 4:
            if int(year) % 400 == 0:
                if int(year) % 100 == 0:
                    if int(year) % 4 == 0:
                        print(year + ' is a leap year')
                    else:
                        print(year + ' is not a leap year')
                else:
                    print(year + ' is a leap year')

            else:
                print(year + ' is not a leap year')
        else:
            print('Enter proper value : ')

        return
###########################################################################################

# This program replaces the given string by <<username>> in the statement

    def stringReplace(self, input, string):
        if len(input) > 3:
            resultString = string.replace('<<UserName>>', input)
            return resultString
        else:
            print('Please enter string greater than 3 characters')

###########################################################################################

#This program prints the number of times the program took to
# generate N number of distinct coupons

    def CouponNumbres(self, distinctCoupons):
        coupon = 0
        flag = 0
        lis_coupons = []
        dist_count = 0;
        count = 0;
        random_no = 0;
        random_no_count = 0;
        flag = 0;

        while(coupon < distinctCoupons):
            randomNumber = random.randint()
            random_no_count +=1
            for i in range(distinctCoupons):
                if lis_coupons[i] != random_no and random_no>0 :
                    flag = 1
            if flag==1 :
                    flag = 0
                    count = count + 1
                    lis_coupons[count] = random_no
                    dist_count+=1
        print('"Total random numbers generated :', random_no_count)
        print('Distinct coupons are :')
        for i in range(distinctCoupons):
            print(lis_coupons[i])

###########################################################################################

# Sum of 3 integers in an array whose addition is 0
    def Time(self):
         return int(time())
