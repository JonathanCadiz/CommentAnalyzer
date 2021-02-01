import comments
import language_processing as lp


def main():
    new_request = comments.VideoRequest(input("Please enter your video's URL\n"))
    new_request.request_comments()
    text_list = []
    for comment in new_request.all_comments:
        print(comment.text)
        text_list.append(comment.text)
    print(len(new_request.all_comments))
    text_string = ".".join(text_list)
    print(text_string)
    print(lp.extract_keywords(text_string))


if __name__ == "__main__":
    main()
