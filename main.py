from stats import num_count, letter_count, letter_sort

def get_book_text():
    with open("/home/jaeger/bookbot/books/frankenstein.txt", "r") as f:
        content = f.read()
    print (content)
    return (content)

g_content = get_book_text()

print("=============================== BOOKBOT =====================================")

print("Analyzing book found at /home/jaeger/bookbot/books/frankenstein.txt...")

print("------------------------------- WORD COUNT ----------------------------------")

num_count(g_content)

print("-------------------------------- CHARACTER COUNT ----------------------------")

g_letter_cnt = letter_count(g_content)

g_letter_sort = letter_sort(g_letter_cnt)

print ("=============================== END =========================================")