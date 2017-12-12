import socket


def UdpClient():
    
    # Socket object creation
    #socket.AF_INET Use of Ipv4 address or hostname
    #socket.SOCK_STREAM UDP Client
    client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM )
    
    return client


def UdpSenderReceiver(client,target_host,target_port):
    Client=UdpClient()
    #Sending some data
    client.sendto("AAABBBCCC",(target_host,target_port))
    
    #Data reception
    data, addr = client.recv(4096)
    
    #Show response
    showData(data)
    
def showData(data):
    #Create your own display data operations
    print data

def main():
    client=UdpClient()
    UdpSenderReceiver(client,"127.0.0.1",1900)

    
if __name__ == "__main__":
    main()