def get_word_count(path):
    with open(path) as f:
        file_contents = f.read()
    return len(file_contents.split())
