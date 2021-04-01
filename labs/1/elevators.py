import math

def elevatorTimes(x, y):
    times = x / y
    print(math.ceil(times))
 
    

elevatorTimes(int(input("how many people?")), int(input("how much capacity?")))


    