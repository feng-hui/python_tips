#!/usr/bin/python3
# -*- coding:utf-8 -*- 
# @author FH
# @email: capricorn1203@126.com
# @time: 2019/1/31 17:38
import unittest
# import socketLogger
import logging
import logging.handlers
import pickle
#import cPickle as pickle


def test_StringReceivedIsSameAsStringSent():
    host = 'localhost'
    port = 9000
    stringSent = "hello world!"
    stringReceived = None
    log_msg = None

    def sendLogToSocket(host,port, stringSent):
        logger = logging.getLogger('mylogger') # to log Led Observer output over a socket
        sh = logging.handlers.SocketHandler(host,port) # handler to write to socket
        logger.addHandler(sh)
        logger.critical(stringSent)
        logger.removeHandler(sh)
        sh.close()

    import threading
    t = threading.Thread(target=sendLogToSocket, args=(host,port,stringSent)) # socket requires 2 different ports if on the same machine
    t.start() # send log in a thread

    import socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #INET => IPv4, STREAM => TCP
    serversocket.bind((host,port)) # 'localhost' => implies only visible within the same machine
    serversocket.listen(1) # accept 1 connection only
    (clientsocket, address) = serversocket.accept()
    chunk = clientsocket.recv(1024)
    print('socketlistener: data received: ', repr(chunk))
    import struct
    slen = struct.unpack(">L", chunk[:4])[0]
    obj = pickle.loads(chunk[4:])
    print('un pickling log: ', repr(obj))
    stringReceived = logging.makeLogRecord(obj)
    #log_msg = logging.makeLogRecord(stringReceived)
    print('socketlistener: converted to log: ', repr(stringReceived))
    clientsocket.close()
    serversocket.close()

    t.join() # wait for the log thread to finish

    print('string sent: ', repr(stringSent), ' received: ', repr(stringReceived.getMessage()))
    assert(stringSent == stringReceived.getMessage())

if __name__ == "__main__":
   test_StringReceivedIsSameAsStringSent()