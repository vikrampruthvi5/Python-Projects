#!/usr/bin/env python3

from datetime import datetime
import requests
import pv_getKey
import pv_time

def get_EUR():
    key = pv_getKey.get_key("DataFixer.txt")
    URL = r'http://data.fixer.io/api/latest?access_key=' + key + '&base=EUR&symbols=INR'
    response = requests.get(URL)
    json_data = response.json()
    ist_time = pv_time.pv_time().get_ist().split('.')[0].split(' ')
    try:
        date_pre_format = datetime.strptime(ist_time[0], '%Y-%m-%d')
        date_post_format = str(datetime.strftime(date_pre_format, '%dth %b %Y'))
        #print(date_post_format+" : "+str(json_data['rates']['INR']))
        return str(date_post_format + "\n"  + ist_time[1] + " : "+str(json_data['rates']['INR']))
    except: 
        print("Failed with ")
    

if __name__ == "__main__":
    get_EUR()

