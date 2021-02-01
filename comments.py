import os
import googleapiclient.discovery
import urllib.parse as urlparse


def comment_request(url):
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # print(response['items'])
    video_id = extract_video_id(url)
    lis = recursive_get(video_id)
    print(len(lis))


def extract_video_id(url):
    url_data = urlparse.urlparse(url)
    query = urlparse.parse_qs(url_data.query)
    video_id = query["v"][0]
    return video_id


def recursive_get(video_id, next_token=0):
    random_list = []
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get("DEVELOPER_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = None

    if next_token != 0:
        request = youtube.commentThreads().list(
            part="snippet, replies",
            maxResults=100,
            pageToken=next_token,
            videoId=video_id
        )
    else:
        request = youtube.commentThreads().list(
            part="snippet, replies",
            maxResults=100,
            videoId=video_id
        )
    
    response = request.execute()

    for comment in response['items']:
        text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        replies_list = []

        if comment['snippet']['totalReplyCount'] > 0:
            print("True")
            print(comment['snippet']['totalReplyCount'])
            # print(comment['replies']['comments'])
            for reply in comment['replies']['comments']:
                comment_reply = reply['snippet']['textDisplay']
                replies_list.append(comment_reply)
        else:
            print("false")

        print(text)
        print(replies_list)
        random_list.append((text, replies_list))

    if 'nextPageToken' in response:
        random_list += recursive_get(video_id, response['nextPageToken'])

    return random_list
