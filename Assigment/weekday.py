import datetime
now = datetime.datetime.now() #gets current date and time
x = now.weekday()#gives numerical value between 0-6 for each day of the week
Days = {0 : "Yes, unfortunately today is a weekday.", 1 : "Yes, unfortunately  today is a weekday.", 2 : "Yes, unfortunately today is a weekday.", 
3: "Yes, unfortunately today is a weekday.", 4 :"Yes, unfortunately today is a weekday.", 5 : "Its is the weekend yay!", 6 :"It is the weekend, yay!"}
#assigns each day of the week to an output 
y = Days[x]
print(y)