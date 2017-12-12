import socket


def TcpClient(target_host,target_port):
    
    # Socket object creation
    #socket.AF_INET Use of Ipv4 address or hostname
    #socket.SOCK_STREAM TCP Client
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    
    #Client connection
    client.connect((target_host,target_port))
    
    return client

def TcpSenderReceiver(client,target_host,target_port):
    Client=TcpClient(target_host,target_port)
    #Sending some data
    client.send("GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
    
    #Data reception
    response = client.recv(4096)
    
    #Show response
    showData(response)
    
def showData(data):
    #Create your own display data operations
    print data

def main():
    target_host="www.example.com"
    target_port=80
    
    client=TcpClient(target_host,target_port)
    TcpSenderReceiver(client,target_host,target_port)
if __name__ == "__main__":
    main()