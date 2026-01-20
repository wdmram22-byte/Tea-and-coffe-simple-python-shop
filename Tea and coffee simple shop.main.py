drink = input(" ● what would you like to drink ?(coffee /tea) :")

if drink == "coffee":
    sugar=input(" ● do you want it black or with sugar ? :")
    
    if sugar =="black":
        print(" black coffee . ")
    elif sugar =="with sugar" :
        print(" coffee with suger is resdy ")
        
elif drink =="tea"  :
    type_of_tea = input(" ● green or red tea ? ")
    if type_of_tea=="green":
        print ("●green tea ready ")
    elif type_of_tea=="red":
        print ("●red tea ready   ")
else:
    print("● sorry we dont sell like that🙂")
