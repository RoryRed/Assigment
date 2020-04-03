#Rory Redmond
#formula for caluating bmi based off user inputs 


height= float(input("Enter Height in cm : "))/100 #formula to convert height in cm to m
Weight= float(input("Enter weight in kg :"))#input of weigt in kg
Bmi = Weight/(height**2)#uses vaules for height and width to calculate BMI
print(Bmi)