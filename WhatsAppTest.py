#!/usr/bin/env monkeyrunner
# encoding=utf-8

#import time and sys module
import time
import sys
#import MonkeyRunner api
from com.android.monkeyrunner import MonkeyRunner ,MonkeyDevice ,MonkeyImage

#generate current time
now=time.strftime("%Y-%m-%d-%H-%M-%S")

#set the location of picture and log
path='E:/picture'
logpath="E:/log"

#get file name
name=sys.argv[0].split("\\")
filename=name[len(name)-1]

#create a log file
log=open(logpath+filename[0:-3]+"-log"+now+".txt",'w')

#create device the two parameters are waiting time and serial number.
device=MonkeyRunner.waitForConnection(5,'7255f2fc')

#install whatsapp apk.
#device.installPackage ('D:\\apk\\whatsapp.apk')

#print operate infomation to log file.
log.write("installing apk\n")

#waiting 2 seconds.
MonkeyRunner.sleep(2)

#launch app.
device.startActivity(component='com.whatsapp/.Main')
MonkeyRunner.sleep(2)
#print operate information.
log.write("Launching app\n")
#take a picture
result = device.takeSnapshot()
#save picture
result.writeToFile(path+"main page"+now+'.png','png')

#tap the desired location(Different size device have different location.)
device.touch(119,366,'DOWN_AND_UP')
MonkeyRunner.sleep(2)


for i in range(1,5):
    device.type("test")
else:
    device.type('OK!')
#take a picture
result1=device.takeSnapshot()
#save picture
result1.writeToFile(path+'.png','png')

#compare the picture to the right picture
resultTrue=MonkeyRunner.loadImageFromFile('E:/right/right1.png')
log.write("comparing picture\n")

if(result.sameAs(resultTrue,0.9)):
    #print information
    print("success")
    #print information to file
    log.write("success\n")
else:
    #print information
    print("fail")
    log.write("fail\n")

#compare the picture to the right picture
resultTrue2=MonkeyRunner.loadImageFromFile('E:/right/right2.png')
log.write("comparing picture\n")

if(result1.sameAs(resultTrue2,0.9)):
    #print information
    print("success")
    #print information to file
    log.write("success\n")
else:
    #print information
    print("fail")
    log.write("fail\n")