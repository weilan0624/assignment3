from pprint import pprint

f=open('finish.txt','r')
count_1=0
count = 0
for line in f:
    if count == 0:
        size = int(line[:-1])
        light = [ [False for i in range(size)] for i in range(size) ]
        count += 1
    else:
        line=line[:-1].replace(","," ").split(" ")
        if line[0] == "turn" and line[1] == "on":
            command = line[0]+line[1]
            x1=int(line[2])
            x2=int(line[-2])
            y1=int(line[3])
            y2=int(line[-1])

            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    light[i][j] = True
        elif line[0] == "turn" and line[1] == "off":
            command = line[0]+line[1]
            x1=int(line[2])
            x2=int(line[-2])
            y1=int(line[3])
            y2=int(line[-1])
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    light[i][j] = False
        elif line[0] == "switch":
            command = line[0]
            x1=int(line[1])
            x2=int(line[-2])
            y1=int(line[2])
            y2=int(line[-1])
            for i in range(x1,x2+1):
                for j in range(y1,y2+1):
                    if light[i][j] == True:
                        light[i][j] = False
                    else:
                        light[i][j] = True
        else:
            continue
lightOn = 0
for i in range(size):
    lightOn += sum(light[i]) 
print(lightOn)

