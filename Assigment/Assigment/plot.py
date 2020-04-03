import numpy as np 
import matplotlib.pyplot as plt

x = np.linspace(0 , 4, 100)#sets range of values beteen 0 and 4 with 100 intervals
fx= x
gx = x**2 #x to the power of two
hx= x**3 #x to the power of three
plt.plot(x, gx, label = "squared") #plots x against gx
plt.plot(x,fx, label ="x = x")    # plots x against fx
plt.plot(x,hx ,label = "cubed") # plts x against
plt.legend() # creates a legend on the plot
plt.title("Relationship between a number to the power of 1 ,2,3") #titles the grapgh
plt.xlabel("Input Range") #titles the x axis
plt.ylabel("Output") # titles the y axis 

plt.show()