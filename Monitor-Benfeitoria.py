import urllib.request
import json
from pprint import pprint
import winsound
import time,sys
from time import gmtime, strftime


oldMoney = 0

def playSound():        
     winsound.Beep(300, 200)
     winsound.Beep(500, 300)
     winsound.Beep(300, 200)
     winsound.Beep(200, 300) 
     winsound.Beep(400, 300)

def proc(resp, locate):
    money=""
    for x in range(locate+48,locate+55):
        money=money+resp[x]
        #print (resp[x])
    return money
while (1):
    
    resp = urllib.request.urlopen("http://benfeitoria.com/startupz2").read()
    locate = str(resp).find("<span>R$</span>")
    #print ("found at ")
    #print (locate)
    money= proc(str(resp), locate)
    #print ("money = ")
    if money != oldMoney:
        print ("Nova Doação !!!")
        playSound()
        time.sleep( 5 )
        
    print ("R$" + money + strftime("em %H:%M:%S de %d/%m/%Y"))    
    oldMoney = money
    time.sleep( 0 )

