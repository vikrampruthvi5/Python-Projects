#!/usr/bin/env python3

def get_key(connection):
    req_key = connection
    DIR = r'/home/pi/Documents/src_git/PVPython/Keys/'
    file = open(DIR+req_key, 'r')

    # Read file and return key
    key = file.readline().strip()
    return key
    
if __name__ == "__main__":
	x = get_key("DataFixer.txt")
