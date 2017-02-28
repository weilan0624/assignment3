from pprint import pprint
import argparse
def turn_on(light,line):
    x1=int(line[2])
    x2=int(line[-2])
    y1=int(line[3])
    y2=int(line[-1])
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            light[i][j]=True
    return light
            
def turn_off(light,line):
    x1=int(line[2])
    x2=int(line[-2])
    y1=int(line[3])
    y2=int(line[-1])
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            light[i][j]=False;
    return light
def switch(light,line):
    x1=int(line[1])
    x2=int(line[-2])
    y1=int(line[2])
    y2=int(line[-1])
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            if light[i][j] == True:
                light[i][j]=False
            else:
                light[i][j]=True
    return light

def main():
    parser = argparse.ArgumentParser("Process input file")
    # at least one argument is required
    parser.add_argument('--input', help='a filename for calculate total light on leds', nargs='+')
    args = parser.parse_args()
    in_argument = args.input
    filename = in_argument[0]
    f=open(filename,'r')
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
                light=turn_on(light,line)
                #pprint(light)
            elif line[0] == "turn" and line[1] == "off":
                command = line[0]+line[1]
                light=turn_off(light,line)
                #pprint(light)
            elif line[0] == "switch":
                command = line[0]
                light=switch(light,line)
                #pprint(light)
            else:
                continue
    On = 0
    for i in range(size):
        On += sum(light[i])
    #print("read from:",f)
    print(On)
    return On