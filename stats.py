def num_count(content):
    word_length = len(content.split())
    print (f"{word_length} words found in the document")

def letter_count(content):
    letters = list(content.lower())
    letter_amt = {}
    for letter in letters:
        if letter not in letter_amt:
            letter_amt[letter] = 0
        letter_amt[letter] += 1
    print (letter_amt)