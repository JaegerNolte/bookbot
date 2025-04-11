import sys

from stats import (
    num_count, 
    letter_count, 
    letter_sort
)

def get_book_text():
    if len(sys.argv) > 1:

        book_text_file = sys.argv[1]

        with open(book_text_file, 'r') as f:
            content = f.read()
        print (content)
        return (content)
    else:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

g_content = get_book_text()

print("=============================== BOOKBOT =====================================")
print(f"Analyzing book found at #placeholder#")
print("------------------------------- WORD COUNT ----------------------------------")
num_count(g_content)
print("-------------------------------- CHARACTER COUNT ----------------------------")
g_letter_cnt = letter_count(g_content)
g_letter_sort = letter_sort(g_letter_cnt)
print ("=============================== END =========================================")
