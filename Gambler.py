#This program prints the number of times a person won and percentage
# of win and loss
import random
import utilityPackage.utility

numberOfBets= int(input('Enter number of times you wnat to gamble: '))
goal = int(input('Enter your goal: '))
money = int(input('Enter amount of money you have: '))
Utility_obj = utilityPackage.utility.utility()
Utility_obj.GambleingMethod(numberOfBets, goal, money)
