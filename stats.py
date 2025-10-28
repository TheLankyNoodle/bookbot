def get_word_count(path):
    with open(path) as f:
        file_contents = f.read()
    return len(file_contents.split())

def sort_on(items):
    return items["num"]

def sorted_dict_list(dict_of_char_and_num):
    new_dicts = []
    for item in dict_of_char_and_num:
        new_dicts.append({"char": item, "num": dict_of_char_and_num[item]})
    new_dicts.sort(reverse = True, key = sort_on)
    return new_dicts

def get_char_counts(path):
    with open(path) as f:
        file_contents = f.read().lower()

    my_dict = {}
    for char in file_contents:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict
