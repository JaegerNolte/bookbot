def num_count(p_content):
    word_length = len(p_content.split())
    print (f"Found {word_length} total words")

def letter_count(p_content):
    letters = list(p_content.lower())
    letter_amt = {}
    for letter in letters:
        no_space = letter.strip()
        if no_space:
            letter_amt[no_space] = letter_amt.get(no_space, 0) + 1
    return (letter_amt)

def letter_sort(p_content):
    sorted_letters = dict(sorted(p_content.items(), key=lambda item: item[1], reverse=True))

    for key, value in sorted_letters.items():
        print (f"{key}: {value}")