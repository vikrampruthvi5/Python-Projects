#!/usr/bin/python
import socket


def Main():
    # host = 'ec2-54-184-91-231.us-west-2.compute.amazonaws.com'
    # host_ip = socket.gethostbyname(host)
    host_ip = ''
    print(host_ip)
    port = 5555

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host_ip, port))

    s.listen(5)
    conn, req = s.accept()
    print("Connection established with " + req[0])

    while True:
        data = conn.recv(1024).decode('utf-8')
        if not data:
            break
        print("From connected user : " + data)
        data = input("Your response : ")
        print("Sending: " + data)
        if data == "close":
            s.close()
            break
        conn.send(data.encode('utf-8'))
    s.close()


if __name__ == '__main__':
    Main()
