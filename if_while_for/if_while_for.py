#!/usr/bin python3
import datetime

def showdatetime():
    print ("Show " + str(datetime.datetime.now())+ "\n")

def countnumbers():
    for i in range(11):
        print (i)

def listcars():   #For with lists
    cars = ['camaro', 'ferrari', 'lamborguini', 'corvette']
    for car in cars:
        print (car)
        
    result = int(input("Do you want to sort the list? [0] No - [1] Yes"))
    
    if result == 1:
        cars.sort()
        print (cars)
    
if __name__ == '__main__':
    print("Hello! The program started")
         
    option = -1
    while option != 99:
        
        option = int(input("Choose one option: \n  0 : Show DateTime Now \n  1 : Count 10 numbers  \n  2 : List Cars \n  99: Exit program \n "))
        
        if option == 0:
            showdatetime()
        if option == 1:
            countnumbers()
        if option == 2:
            listcars()
        if option == 99:
            break
        else:
            print ("Invalid Option")
            continue
        
    print ("Program Finished")        
        
        
        
    
