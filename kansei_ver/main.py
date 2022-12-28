# -*- coding: utf-8 -*-
import requests
import json
import stu_ID3
import getData
#import testlogin
import threading
import time
idbox = []
#ffff = 0

def postData(data):
    if(data is None):
        print("params is empty")
        return False
    
    payload = {
        "data": data
    }
    #url = "https://script.google.com/macros/s/AKfycbxfqrwe7hTbVKLWxf40Fysqc4QNan2x_L3-pQO8_NkWCIKRL5z9/exec"
    url = "https://script.google.com/macros/s/AKfycbwlwCtvzQuE8Et2__ZiXw2GOwzCDs3fvjSw312q-AT5Mt5x3BU/exec"
    headers = {
        'Content-Type': 'application/json',
    }
    
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    #DB = getData.getData()
    #print(data)
    #for db in DB:
    #   if db["student_id"] == str(data) :
    #        stid = db["id"]
    #        stpass = db["pass"]
    #        flag = int(db["state"])
    #        email = stid+"@mail4.doshisha.ac.jp"
    #        print(stid,stpass,flag,email)
    if(response.status_code == 200 ):
        #print("post success!")
        print("------------------------")
        print(response.text)
        print("------------------------")
        return True
    #print(response.text)
    #print("------------------------")
    return False

def looplogin():
    while(True):
        try:
            while idbox:
                time.sleep(10)
                data=idbox.pop(0)
                DB = getData.getData()
                for db in DB:
                    if db["student_id"] == str(data) :
                        stid = db["id"]
                        stpass = db["pass2"]
                        flag = int(db["state"])
                        global ffff
                        ffff = flag
                        email = stid+"@mail4.doshisha.ac.jp"
                testlogin.loginQR(email,stid,stpass,flag)
        except Exception as e:
            print("S")
            continue
            
def main():
    #th=threading.Thread(target=looplogin)
    #th.start()
    while True:
        #try:
            time.sleep(2)
            id = stu_ID3.studentID()
            id.getID()
            global idbox 
            idbox.append(id.student_id)
            print(idbox)
            postData(id.student_id)
        #except:
            print("V")
            
                              
   
if __name__ == '__main__':
    #while True:
        #try:
    main()
        #except KeyboardInterrupt:
            #exit()
        #except Exception as e:
            #print(e)
           # continue
