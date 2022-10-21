#Color      Time Req        Cost        Dye     Price       Profit
#-------------------------------------------------------------------
#White      0               5           12      12          7
#Blue       20              7           10      15          8
#Yellow     20              7           15      15          8
#Red        40              10          12      16          6

#Goal to sell 50 shirts, what is the max profit
shirtCost = [5,7,7,10]
shirtPrice = [12,15,15,16]
shirtDye = [50,10,15,12]
shirtTimes = [0,20,20,40]
i = 0
def finder(i):
    shirtNum = shirtDye[i]
    x=int(shirtNum)
    y=(shirtPrice[i]*x)-(shirtCost[i]*x)
    if(i == 0):
        type = 'White   '
        timeReq = shirtTimes[i]
        #shirtNum1 = str(shirtNum[i])
    elif(i == 1):
        type = 'Blue    '
        timeReq = shirtTimes[i]
        #shirtNum1 = shirtNum[i]
    elif(i == 2):
        type = 'Yellow  '
        timeReq = shirtTimes[i]
        #shirtNum1 = shirtNum[i]
    elif(i == 3):
        type = 'Red     '
        timeReq = shirtTimes[i]
        #shirtNum1 = shirtNum[i]
    else: type = 'null'
    print('Profit of ',type,'$',str(y),' for',x,'shirts','    as well as',timeReq,'minutes to make')
    if(i < 3):
        i = i+1
        finder(i)
    else: print('Profit for max shirts possible per color')
    
finder(i)

#This currently calculates how much profit you would make if you sold as many as you could of every
#individual type of shirt