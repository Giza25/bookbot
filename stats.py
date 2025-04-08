def sort_on_value(dict):
    return dict["num"]

def get_num_of_words(words):
    list = words.split()
    return len(list)

def get_num_of_char(text):
    text = text.lower()
    chars = {}
    for i in text:
        if i not in chars:
            chars[i] = 1
        else:
            chars[i] += 1
    return chars

def sort_dict_by_value(dict):
    sorted_dict = []
    for char in dict:
        sorted_dict.append({"char" : char, "num" : dict[char]})
    sorted_dict.sort(reverse=True, key=sort_on_value)
    return sorted_dict