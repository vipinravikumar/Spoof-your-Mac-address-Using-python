# Spoof-your-Mac-address-Using-python
#Do check out my video on yt:https://bit.ly/3smb0u6
#This is a Linux Compatible Code so it wont work on other os
#NOTE: USE THE FOLLOWING CODE FOR LEGGITIMATE REASONS ONLY
import os
import subprocess 
import random

def get_rand():
    return random.choice("abcdef0123456789") 

def new_mac():
    new_ = "" 
    for i in range(0,5):
        new_ += get_rand() + get_rand() + ":"  
    new_ += get_rand() + get_rand() 
    return new_

print'Old_Mac_Address'
print(os.system("ifconfig eth0 | grep ether | grep -
oE [0-9abcdef:]{17}")) 
subprocess.call(["sudo","ifconfig","eth0","down"]) 
new_m = new_mac() 
subprocess.call(["sudo","ifconfig","eth0","hw","ether","
%s"%new_m]) 
subprocess.call(["sudo","ifconfig","eth0","up"]) 
print'New_Mac_Address'                 
print(os.system("ifconfig eth0 | grep ether | grep -
oE [0-9abcdef:]{17}"))
