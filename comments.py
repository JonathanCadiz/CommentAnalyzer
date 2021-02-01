import os
import googleapiclient.discovery
import urllib.parse as urlparse


def comment_request(url):
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # print(response['items'])
    video_id = extract_video_id(url)
    lis = recursive_get(video_id, 0)
    print(len(lis))


def extract_video_id(url):
    url_data = urlparse.urlparse(url)
    query = urlparse.parse_qs(url_data.query)
    video_id = query["v"][0]
    return video_id


def recursive_get(video_id, token):
    random_list = []
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = os.environ.get("DEVELOPER_KEY")

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=DEVELOPER_KEY)

    request = None

    if token != 0:
        request = youtube.commentThreads().list(
            part="snippet",
            maxResults=100,
            pageToken=token,
            videoId=video_id
        )
    else:
        request = youtube.commentThreads().list(
            part="snippet",
            maxResults=100,
            videoId=video_id
        )
    
    response = request.execute()

    for comment in response['items']:
        text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
        print(text)
        random_list.append(text)

    if 'nextPageToken' in response:
        random_list += recursive_get(video_id, response['nextPageToken'])

    return random_list
