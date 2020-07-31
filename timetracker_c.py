#Time Tracking code
#Group members: Winston Best-Ezeani, Sybil Meselebe and Theresa Allotey
from datetime import datetime as dt
import csv

#MAIN FUNCTION
def timeTracker():

	print ("Welcome to our Time Tracking App\n")

	task = input("Please enter the type of the task to begin: ")

	#Get the start and end date and times using these user defined functions
	startDate = getDatetime("start")
	endDate = getDatetime("end")

	#Calculate hours spent

	'''find duration'''
	duration = endDate - startDate

	'''compute total time spent in hours'''
	t_time = duration.total_seconds()/60**2
	
	#Calculate money made
	amount = pay_per_hour(t_time)
	
	#Create a list of task details for writing to csv
	taskList = [task, startDate, endDate, t_time, amount]

	#Write details to a csv file
	with open(r'timetracking.csv', 'a', newline='') as file:
		csv.writer(file).writerow(taskList)
		
	
	result = "\nNana worked for " + str(t_time) + " hours, between " + str(startDate) + " and " + str(endDate) + ". He should be paid $" + str(amount) + "."

	print (result)


'''OTHERS'''

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


#Function to calculate the pay per hour
def pay_per_hour(hours):
	amount = round(5 * hours, 2)
	return amount


if __name__ == "__main__":
    timeTracker()			
