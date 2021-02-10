import os
import googleapiclient.discovery
import urllib.parse as urlparse


class Comment:
    def __init__(self, text, comment_id, comment_type, reply_count=0,
                 like_count=0, published_time=None):
        self.text = text
        self.comment_id = comment_id
        self.comment_type = comment_type
        self.reply_count = reply_count
        self.like_count = like_count
        self.published_time = published_time
        self.replies = []

    def add_reply(self, reply):
        self.replies.append(reply)


class VideoRequest:
    def __init__(self, url, key=None):
        self.url = url
        self.video_id = self.__extract_id()
        self.main_comments = []
        self.all_comments = []
        self.key = key
        self.top_comment = {}
    
    def __extract_id(self):
        url_data = urlparse.urlparse(self.url)
        query = urlparse.parse_qs(url_data.query)
        video_id = query['v'][0]
        return video_id

    def request_comments(self):
        comment_list = []
        all_comments_list = []
        top_comment = {
            "text": '',
            "likes": 0
        }
        api_service_name = "youtube"
        api_version = "v3"
        if self.key is None:
            DEVELOPER_KEY = os.environ.get("DEVELOPER_KEY")
        else:
            DEVELOPER_KEY = self.key

        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey=DEVELOPER_KEY)

        next_token = 0

        while True:
            if next_token != 0:
                request = youtube.commentThreads().list(
                    part="snippet, replies",
                    maxResults=100,
                    pageToken=next_token,
                    videoId=self.video_id
                )
            else:
                request = youtube.commentThreads().list(
                    part="snippet, replies",
                    maxResults=100,
                    videoId=self.video_id
                )
            response = request.execute()
            for comment in response['items']:
                text = comment['snippet']['topLevelComment']['snippet']['textOriginal']
                comment_id = comment['snippet']['topLevelComment']['id']
                comment_type = "top"
                reply_count = comment['snippet']['totalReplyCount']
                like_count = comment['snippet']['topLevelComment']['snippet']['likeCount']
                published_time = comment['snippet']['topLevelComment']['snippet']['publishedAt']

                new_comment = Comment(text, comment_id, comment_type,
                                      reply_count, like_count, published_time)

                if new_comment.reply_count > 0:
                    for reply in comment['replies']['comments']:
                        reply_text = reply['snippet']['textOriginal']
                        reply_id = reply['id']
                        reply_type = "reply"
                        reply_likes = reply['snippet']['likeCount']
                        reply_time = reply['snippet']['publishedAt']
                        reply_comment = Comment(reply_text, reply_id, reply_type,
                                                like_count=reply_likes, published_time=reply_time)
                        new_comment.replies.append(reply_comment)
                        all_comments_list.append(reply_comment)

                if new_comment.like_count > top_comment['likes']:
                    top_comment = {
                        "text": new_comment.text,
                        "likes": new_comment.like_count
                    }

                comment_list.append(new_comment)
                all_comments_list.append(new_comment)

            if 'nextPageToken' in response:
                next_token = response['nextPageToken']
            else:
                break

        self.top_comment = top_comment
        self.main_comments = comment_list
        self.all_comments = all_comments_list
