import os
from slackclient import slackrequest, SlackClient
import requests


def post_slack_message(message):
    # slack_token = os.environ["SLACK_API_TOKEN"]
    slack_token='xoxp-393473516853-392784516193-428903814870-623c25adc6bd4e2764fa76a1e944990a'
    print(slack_token)
    sc = SlackClient(slack_token)

    sc.api_call(
      "chat.postMessage",
      channel="spy-cam-opencv",
      text= message+" :tada:"
    )


def post_slack_image(image):
    try:
        image = 'SocketProgramming/' + image
        my_file = {
                      'file' : (image, open(image, 'rb'), 'png')
        }
        payload={
            "filename":image,
            "token":'xoxp-393473516853-392784516193-428903814870-623c25adc6bd4e2764fa76a1e944990a',
            "channels" : ["spy-cam-opencv"]
        }

        print(payload['filename'])

        r = requests.post("https://slack.com/api/files.upload", params=payload, files=my_file)
        print(r)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    post_slack_image('test.png')