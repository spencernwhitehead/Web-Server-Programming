#Spencer Whitehead
#1001837401
from socket import *
from _thread import *
import os

#thread function
#takes in connection socket and processes connection request
def processRequest(connectionSocket):
    #this try block may not need to be here (it was used to test the client program) but it doesn't hurt
    try:
        #decode client request
        requestData = connectionSocket.recv(1024).decode('utf-8')
    except ConnectionResetError:
        print('connection ended')
        return None
    
    print(requestData)

    #take request data and pull out the file request if there is one
    parsedRequestData = requestData.split()
    getReq = ''
    if len(parsedRequestData) > 1 and len(parsedRequestData[1]) > 1:
        getReq = parsedRequestData[1][1:]
    print(getReq)

    #default response, should always get overwritten
    http_response = b"""HTTP/1.1 200 OK\r\n\r\nyou shouldn't be able to see this"""

    #if getReq == 'index1.html':
    #    getReq == 'index.html'

    #if client requests an existing valid file, the file is opened and appended to the http response
    if getReq == 'index.html':
        file = open(os.path.realpath(os.path.dirname(__file__)) + '\\' + getReq, 'rb')
        http_response = b"HTTP/1.1 200 OK\r\nContent Type: text/html\r\n\r\n" + file.read()
        file.close()
    elif getReq == 'guy.jpg':
        file = open(os.path.realpath(os.path.dirname(__file__)) + '\\' + getReq, 'rb')
        http_response = b"HTTP/1.1 200 OK\r\nContent Type: image/jpeg\r\n\r\n" + file.read()
        file.close()
    #error handling for if user goes to /index1.html
    #will send 301 with new location of /index.html
    elif getReq == 'index1.html':
        http_response = b"""HTTP/1.1 301 Moved Permanently\r\nLocation: /index.html"""
    #error for if user requests a file that hasn't been defined
    else:
        http_response = b"""HTTP/1.1 404\r\n\r\nError 404: file not found"""
    
    #send response and end connection
    connectionSocket.sendall(http_response)
    connectionSocket.close()
    print('connection ended')

if __name__ == "__main__":
    #create server socket and set to listen for new connections
    serverPort = 8080
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print('The server is ready to receive')

    #while loop constanty runs with main thread
    #whenever a new connection is created, a new thread will be created to process the request
    while True:
        connectionSocket, addr = serverSocket.accept()
        print('new connection created')
        start_new_thread(processRequest, (connectionSocket,))