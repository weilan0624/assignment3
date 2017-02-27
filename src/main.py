#http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt
#http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_a.txt
#http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_b.txt
#http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_c.txt
#http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3_d.txt

import urllib.request

def read_file():
    uri = "http://claritytrec.ucd.ie/~alawlor/comp30670/input_assign3.txt"    
    req = urllib.request.urlopen(uri)
    buffer=req.read().decode('utf-8')