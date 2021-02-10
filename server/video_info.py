import os
import googleapiclient.discovery
import urllib.parse as urlparse


class VideoInfoRequest:
    def __init__(self, url, key=None):
        self.url = url
        self.video_id = self.__extract_id()
        self.key = key
        self.publishedAt = ''
        self.title = ''
        self.thumbnail = ''
        self.channel = ''
        self.tags = []
        self.views = 0
        self.likes = 0
        self.dislikes = 0
        self.commentCount = 0

    def __extract_id(self):
        url_data = urlparse.urlparse(self.url)
        query = urlparse.parse_qs(url_data.query)
        video_id = query['v'][0]
        return video_id

    def request_info(self):
        api_service_name = "youtube"
        api_version = "v3"
        if self.key is None:
            DEVELOPER_KEY = os.environ.get("DEVELOPER_KEY")
        else:
            DEVELOPER_KEY = self.key

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

        request = youtube.videos().list(
            part="snippet,statistics",
            id=self.video_id
        )
        response = request.execute()['items'][0]
        stats = response['statistics']
        details = response['snippet']

        self.views = stats['viewCount']
        self.likes = stats['likeCount']
        self.dislikes = stats['dislikeCount']
        self.commentCount = stats['commentCount']

        self.publishedAt = details['publishedAt']
        self.title = details['title']
        self.thumbnail = details['thumbnails']['high']['url']
        self.channel = details['channelTitle']
        if 'tags' in details:
            self.tags = details['tags']

