#Module 5 assigment
NBR_OF_DAYS = 7

while (keepGoing=="y"):
    totalBottles = 0
    counter = 0
    todayBottles = 0
    totalPayout = 0
    while(counter < NBR_OF_DAYS):
        todayBottles = int(input("Enter bottles for day #"+ str(counter + 1) +": "))
        totalBottles = totalBottles + todayBottles
        counter = counter + 1
    PAYOUT_PER_BOTTLE = .10
    totalPayout = totalBottles * PAYOUT_PER_BOTTLE
    print("\nThe total number of bottles : "+ str(totalBottles))
    print("The total pay out is: %.2f" % totalPayout)
    keepGoing = input("\nDo you want to enter another week's worht of data?(y for yes or n for no): ")
