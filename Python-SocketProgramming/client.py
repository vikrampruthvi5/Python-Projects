#!/usr/bin/python

import socket, time
from SocketProgramming import cv_final
from SocketProgramming.slack_message import post_slack_message as psm
from SocketProgramming.slack_message import post_slack_image as psi
from os import system
from cv2 import imwrite, destroyAllWindows


def Main(x):
    try:
        # host = 'ec2-54-184-91-231.us-west-2.compute.amazonaws.com'
        # host_ip = socket.gethostbyname(host)
        host_ip = ''
        print(host_ip)
        port = 5555

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host_ip, port))
        message = "Hai Server, this is your client... Greetings..."
        while message != 'q':
            s.send(message.encode('utf-8'))
            data = s.recv(1024).decode('utf-8')
            print("Received from server: " + data)

            # Record 30 sec video
            if data == 'get_vid':
                try:
                    cv_final.set_video_env()
                    s.send('Video recording in progress...'.encode('utf-8'))
                    continue
                except:
                    print("Video capturing failed")

            elif data == 'get_pic':
                try:
                    x = cv_final.get_pic()
                    print(type(x))
                    imwrite('test.png', x)
                    s.send('image processed'.encode('utf-8'))
                    destroyAllWindows()
                    psi('test.png')
                    cv_final.del_file('test.png')
                    continue
                except Exception as e:
                    print(e)
            elif data == 'close':
                message = 'q'
                s.close()
                exit(0)
            else:
                s.send('Anything else...'.encode('utf-8'))
        s.close()
    except Exception as e:
        print("\n*** PLEASE DO NOT TERMINATE THE PROCESS ***\nServer offline.\nRetrying...\n")
        system('export SLACK_API_TOKEN=\'xoxp-393473516853-392784516193-428903814870-623c25adc6bd4e2764fa76a1e944990a\'')
        if x is 1:
            psm("Client is trying to connect... ")
            x = 0
        time.sleep(3)
        Main(x=0)


if __name__ == '__main__':
    Main(x=1)
