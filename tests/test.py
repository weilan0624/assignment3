from nose.tools import *
from src.try2 import *
from src.ledtester import lightOn

'''def test():
    filename='1.txt'
    buffer=read_file(filename=filename)
    eq_(len(buffer),9140,"buffer size do not match")'''

def count():
    size=10;
    line="turn on 0,0 through 9,9"
    line="turn off 0,0 through 9,9"
    count=lightOn
    eq_(count,0,"count:[]".format(count))
