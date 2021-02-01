import comments


def main():
    new_request = comments.VideoRequest(input("Please enter your video's URL\n"))
    new_request.request_comments()
    for comment in new_request.all_comments:
        print(comment.text)
    print(len(new_request.all_comments))


if __name__ == "__main__":
    main()
