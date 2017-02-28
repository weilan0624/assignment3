from nose.tools import *
from src.main import *


def test_turn_on():
    size=4;
    light = [ [False for i in range(size)] for i in range(size) ]
    line=["turn", "on", "0","0" ,"through" ,"3","3"]
    answer=[[True, True, True, True],
             [True, True, True, True],
             [True, True, True, True],
             [True, True, True, True]]
    eq_(turn_on(light,line),answer,"not fjj")

def test_turn_off():
    size=4;
    light = [ [True for i in range(size)] for i in range(size) ]
    line=["turn", "off", "0","0" ,"through" ,"1","1"]
    answer=[[False, False, True, True],
             [False, False, True, True],
             [True, True, True, True],
             [True, True, True, True]]
    eq_(turn_off(light,line),answer,"not fjj")

        