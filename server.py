#导入socket模块
import socket

if __name__ == '__main__':
    # 创建tcp服务端套接字
    # 参数同客户端配置一致，这里不再重复
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    # 设置端口号复用，让程序退出端口号立即释放，否则的话在30秒-2分钟之内这个端口是不会被释放的，这是TCP的为了保证传输可靠性的机制。
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
   
    # 给客户端绑定端口号，客户端需要知道服务器的端口号才能进行建立连接。IP地址不用设置，默认就为本机的IP地址。
    tcp_server.bind(("", 25565))
   
    # 设置监听
    # 128:最大等待建立连接的个数， 提示： 目前是单任务的服务端，同一时刻只能服务与一个客户端，后续使用多任务能够让服务端同时服务与多个客户端
    # 不需要让客户端进行等待建立连接
    # listen后的这个套接字只负责接收客户端连接请求，不能收发消息，收发消息使用返回的这个新套接字tcp_client来完成
    tcp_server.listen(128)
   
    # 等待客户端建立连接的请求, 只有客户端和服务端建立连接成功代码才会解阻塞，代码才能继续往下执行
    # 1. 专门和客户端通信的套接字： tcp_client
    # 2. 客户端的ip地址和端口号： tcp_client_address
    tcp_client, tcp_client_address= tcp_server.accept()
    
    # 代码执行到此说明连接建立成功
    print("客户端的ip地址和端口号:", tcp_client_address)
   
    while True:
        recv_data = tcp_client.recv(1024)
        # 将接收到的服务器数据recv_data通过decode方法解码为utf-8
        print(recv_data.decode(encoding = 'utf-8'))
