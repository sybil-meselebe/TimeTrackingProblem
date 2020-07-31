# TimeTrackingProblem
A Time Tracking Problem in Python

Business Problem:

Nana recently started a consulting business where he is paid based on the number of hours and minutes he works on client projects.He needs a time tracking program, where he enters the date and the time he started working on a task, and then the date and time when he finished a particular task. The program calculates the hours he spent on a task. It then calculates the amount of money Nana made tackling the task. Note that: Nana is paid $5 dollars per hour.
If Nana works from 11AM to 1:30 PM on Monday 27th July, he would make 2.5 X 5 = $12.5 dollars.

# Task
Write a program that would help Nana track his money.
The program calculates the hours he spent on a task.
It then calculates the amount of money Nana made tackling the task. 
Time entered and information from the program should be stored in a csv or excel file for future referencing.

# Our Approach
1. We created a function that collects datetime from the user for start and end dates - 'getDatetime()'
2. We then created a main time tracking function that calls the getDatetime() function and assigns the date returned to start and end dates
3. We computed the hours spent by manipulating time_seconds() function from the datetime module.
4. We then calaculating how much he makes by calling a function we created for calculating his pay per the # of hours.
5. Finally we input the desired values to a list and write to a csv.
6. The program returns a string summary of the users time tracking.
