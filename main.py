def get_book_text():
    with open("/home/jaeger/bookbot/books/frankenstein.txt", "r") as f:
        content = f.read()
    print (content)
    return (content)

def num_count():
    content = get_book_text()
    text = len(content.split())
    print (f"{text} words found in the document")

num_count()