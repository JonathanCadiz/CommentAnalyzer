import comments
import language_processing as lp


def main():
    new_request = comments.VideoRequest(input("Please enter your video's URL\n"))
    new_request.request_comments()

    for comment in new_request.all_comments:
        print(comment.text)

    processed = lp.LanguageProcessing(new_request.all_comments)
    processed.add_unwanted(["video"])
    processed.extract_keywords()
    print(processed.words)
    print(processed.nouns)
    print(processed.adj)
    print(processed.verbs)
    print(processed.links)


if __name__ == "__main__":
    main()
