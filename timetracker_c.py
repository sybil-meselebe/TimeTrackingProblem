#Time Tracking code
from datetime import datetime as dt
import csv


#Function to get the start and end times from the user
def getDatetime(ttype): #ttype sepcifies wether it is a start or end
    isValid=False
    while not isValid:
        u_input = input("Please enter the " + ttype + " date and time (dd/mm/yyyy HH:MM) : ")
        try: 
        # strptime throws an exception if the input doesn't match the pattern
            result = dt.strptime(u_input, "%d/%m/%Y %H:%M")
            isValid=True
        except:
            print ("Please try again with the right format!\n")
			
    return result
