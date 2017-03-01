import os
import re
from pprint import pprint
#find the file whether it exist
filename=input('enter a file name:')
if not os.path.isfile(filename):
     print('File'  + filename + ' does not exist.')
else: 
    f=open(filename,'r')
    count_1=0
    count = 0
#find the file then read each line in the file 
    for line in f:
        if count == 0:
            size = int(line[:-1])
            light = [ [False for i in range(size)] for i in range(size) ]
            count += 1
        else:
#find the command in the line and then cut out the number 
            line=line[:-1].replace(","," ").split(" ")
            if line[0] == "turn" and line[1] == "on":
                command = line[0]+line[1]
#give the first number to x1 second to y1 third number to x2 the last number to y2
                x1=int(line[2])
                x2=int(line[5])
                y1=int(line[3])
                y2=int(line[6])
                if x1<0:
                    x1=0
                if y1<0:
                    y1=0
                if x2>=size:
                    x2=size-1
                if y2>=size:
                    y2=size-1 
                for i in range(x1,x2+1):
                    for j in range(y1,y2+1):
                        light[i][j] = True
                
            elif line[0] == "turn" and line[1] == "off":
                command = line[0]+line[1]
                x1=int(line[2])
                x2=int(line[5])
                y1=int(line[3])
                y2=int(line[6])
                if x1<0:
                    x1=0
                if y1<0:
                    y1=0
                if x2>=size:
                    x2=size-1
                if y2>=size:
                    y2=size-1 
                for i in range(x1,x2+1):
                    for j in range(y1,y2+1):
                        light[i][j] = False
                
            elif line[0] == "switch":
                command = line[0]
                x1=int(line[1])
                x2=int(line[4])
                y1=int(line[2])
                y2=int(line[5])
                if x1<0:
                    x1=0
                if y1<0:
                    y1=0
                if x2>=size:
                    x2=size-1
                if y2>=size:
                    y2=size-1 
                for i in range(x1,x2+1):
                    for j in range(y1,y2+1):
                        if light[i][j] == True:
                            light[i][j] = False
                        else:
                            light[i][j] = True
                
            else:
                continue
#after putting the number into the 2D list and then count the number of True (which means the light is on)
    lightOn = 0
    for i in range(size):
        lightOn += sum(light[i]) 
    print(lightOn)
    
