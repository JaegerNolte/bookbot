from stats import num_count

def get_book_text():
    with open("/home/jaeger/bookbot/books/frankenstein.txt", "r") as f:
        content = f.read()
    print (content)
    return (content)

content = get_book_text()

num_count(content)