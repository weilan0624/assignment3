import os
'''filename = input('enter a file name:')
if not os.path.isfile(filename) :
  print('File ' + filename + ' does not exist.')
else:'''

result=[]
i=""
f=open('finish.txt','r')
light=False;
for line in f:
    line=line[:-1].replace(","," ").split(" ")
    print(line)
    if line[0] == "turn" and line[1] == "on":
        command = line[0]+line[1]
        print(command)
        x1=line[2]
        x2=line[-2]
        y1=line[3]
        y2=line[-2]
        print(x1, y1, x2, y2)
    elif line[0] == "turn" and line[1] == "off":
        command = line[0]+line[1]
        print(command)
        x1=line[2]
        x2=line[-2]
        y1=line[3]
        y2=line[-2]
        print(x1, y1, x2, y2)
    elif line[0] == "switch":
        command = line[0]
        print(command)
        x1=line[1]
        x2=line[-2]
        y1=line[2]
        y2=line[-2]
        print(x1, y1, x2, y2)
    else:
        continue
x11=int(x1)
y11=int(y1)        
x22=int(x2)                
y22=int(y2) 
if command=="turnon":
    for i in range(x11,x22):
        for j in range(y11,y22):
            light=True;
    print(light)
           
    
