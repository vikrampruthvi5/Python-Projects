# Facebook Automation

#Imports
import requests

print("Facebook Python Automation")

token = 'f2890e2ae51731786d25719a88ed0e40'

#URLs
me = 'https://graph.facebook.com/V2.9/me?access_token='+token

x = requests.get(me)

print(x.text)
