import numpy
import cv2, time, os, boto3
from _datetime import datetime
from botocore.client import Config
from os import path, environ
from sys import platform
from os.path import expanduser
from SocketProgramming import slack_message

def get_pic():
    cap = cv2.VideoCapture(0)  # Capture video from camera
    x, y = cap.read()
    cap.release()
    return y


def actual_vid_recording(cap, out):
    counter = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # frame = cv2.flip(frame,0)

            # write the flipped frame
            out.write(frame)
            counter += 1

            # cv2.imshow('frame', frame)
            # if (cv2.waitKey(1) & 0xFF) == ord('q'):  # Hit `q` to exit
            #   break
            if counter == 200:
                break
        else:
            break

    # Release everything if job is finished
    out.release()
    cap.release()
    cv2.destroyAllWindows()


def set_video_env():
    cap = cv2.VideoCapture(0)  # Capture video from camera

    # Get the width and height of frame
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)

    dt = datetime.now()

    file_name = "{}{}{}_{}{}".format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    # Check the type of the machine

    # If machine type is MAC, returns file path with .mp4 format
    if platform == 'darwin':

        desk_path = expanduser("~") + '/'
        file = file_name + '.mp4'
        file_name = desk_path + file
        print(file_name)
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Be sure to use the lower case
        out = cv2.VideoWriter(file_name, fourcc, 20.0, (width, height))
        actual_vid_recording(cap, out)
        export_to_s3(file_name, file)
        del_file(file_name)
    elif platform == 'win32':
        desk_path = path.join(environ["HOMEPATH"], "Desktop") + '\\'
        file = file_name + '.avi'
        file_name = desk_path + file
        print(file_name)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(file_name, fourcc, 20.0, (640, 480))
        actual_vid_recording(cap, out)
        export_to_s3(file_name, file)
        del_file(file_name)


def export_to_s3(path, file):
    try:

        ACCESS_KEY_ID = 'AKIAJJLBIWVDU5YNY4IQ'
        ACCESS_SECRET_KEY = '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'
        BUCKET_NAME = 'datapv5'
        filename = path
        data = open(filename, 'rb')

        s3 = boto3.resource(
            's3',
            aws_access_key_id=ACCESS_KEY_ID,
            aws_secret_access_key=ACCESS_SECRET_KEY,
            config=Config(signature_version='s3v4')
        )
        s3.Bucket(BUCKET_NAME).put_object(Key=file, Body=data)
        message = "{} : {}".format("File uploaded to s3", file)
        slack_message.post_slack_message(message)
    except Exception as e:
        print("Could not import video to S3\n")
        print(e)


def del_file(file_name):
    try:
        os.remove(file_name)
    except Exception as e:
        print("Cannot delete file")



if __name__ == "__main__":
    set_video_env()
