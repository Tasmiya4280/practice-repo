year = int(input("Enter the year: "))

if year % 100 == 0 and year % 400 == 0 :
    print( "The year {} is a leap year".format(year))
elif year % 4 == 0 and year % 100 != 0 :
    print("The year {} is a leap year".format(year))
else:
    print("The year {} is  NOT a leap year".format(year))