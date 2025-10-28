from stats import get_word_count
from stats import get_char_counts
from stats import sorted_dict_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "./books/frankenstein.txt"
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(path)} total words")
    print("--------- Character Count -------")
    dict_list = sorted_dict_list(get_char_counts(path))
    for i in dict_list:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()

