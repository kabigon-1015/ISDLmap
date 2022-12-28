#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import binascii
import nfc
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

clf = nfc.ContactlessFrontend('usb:054c:06c3')

class studentID:
    
    def __init__(self,student_id = 0,service_code2 = 0x1A8B,flag=0):
        #弊学の学生証の学籍番号が格納されているサービスコード
        self.student_id = student_id
        self.service_code2 = service_code2
        self.flag = 0 

    def connected(self,tag):
        if isinstance(tag, nfc.tag.tt3.Type3Tag):
            try:
                idm, pmm = tag.polling(system_code = 0x8BB3)
                tag.idm, tag.pmm, tag.sys = idm, pmm, 0x8BB3 
            
               #16ビットのservice_codeからservice >> 6で上位10ビットを取り出し、service_code && 0x3fで下位6ビットを取り出す
                svcd2 = nfc.tag.tt3.ServiceCode(self.service_code2 >> 6, self.service_code2 & 0x3f)
           
                tag.dump()
           
               #serviceはread_without_encryptionの引数service_list内でのインデックス
                blcd2 = nfc.tag.tt3.BlockCode(0,service=0)
                #read_without_encryptionでタグの指定した部分の情報内のブロックデータを読み取る
                block_data2 = tag.read_without_encryption([svcd2], [blcd2])
                #今回ではブロックデータの1文字目から8文字目に格納されている、それを文字列に変換しutf-8でデコード
                student_id2 = int(block_data2[2:12].decode("utf-8"))
                self.student_id = student_id2
                #idbox.extend(student_id2)
                #print(student_id2)
                #sound = AudioSegment.from_mp3("sound.mp3")
                #play(AudioSegment.from_mp3("sound.mp3"))
                playsound("sound.mp3")
                
                print("学生IDを読み取りました")
                self.flag = 1
            except Exception as e:
                print("学生IDの取得に失敗しました")
                playsound("sound.mp3")
                #play(AudioSegment.from_mp3("sound.mp3"))
                #play(AudioSegment.from_mp3("sound.mp3"))
                #print("Error:%s" % e)
        else:
            print("Error:tag isn't Type3Tag")

        #値をTrueで返すと触れて離すまでの間、一回だけ処理を行う
        return True

    
    def _setID(self):
        
        while True:
            print("学生証をかざしてください")
            #学生証を読み取るまで待機
            clf.connect(rdwr={'on-connect': self.connected,})
            #print(self.student_id)
            if self.student_id != 0:
                #print("finish")
                break

    def getID(self):
        try:
            self._setID()
        except KeyboardInterrupt:
            print("Forced termination")
            clf.close()
            sys.exit(0)
