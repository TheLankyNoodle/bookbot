from stats import get_word_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    print(f"Found {get_word_count("./books/frankenstein.txt")} total words")

main()

