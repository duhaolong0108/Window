""""""
import socket

if __name__ == '__main__':

    # 1 创建客户端套接字对象tcp_client_1
    # 参数介绍：AF_INET 代表IPV4类型, SOCK_STREAM代表tcp传输协议类型 ,注：AF_INET6代表IPV6
   
    tcp_client_1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # 2 通过客户端套接字的connect方法与服务器套接字建立连接  
    # 参数介绍：前面的ip地址代表服务器的ip地址，后面的61234代表服务端的端口号 。
    
    tcp_client_1.connect(("152.70.113.69",44038))
    
    # 将接收到的服务器数据recv_data通过decode方法解码为utf-8
    print(recv_data.decode(encoding = 'utf-8'))

    # 5 最后关闭客户端套接字连接
    tcp_client_1.close()
