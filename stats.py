def count_words(book_text):
    return len(book_text.split())

def count_characters(book_text):
    lower_case_text = book_text.lower()

    char_count_dict = {}

    for c in lower_case_text:
        if not c in char_count_dict:
            char_count_dict[c] = 1
        else:
            char_count_dict[c] += 1

    return char_count_dict

def print_chars(char_dict):
    char_dict_list = []

    for cd in char_dict:
        if cd.isalpha():
            char_dict_list.append({"Character":cd, "Count":char_dict[cd]})

    char_dict_list.sort(reverse=True, key=sort_on)

    for entry in char_dict_list:
        print(f"The {entry["Character"]} character was found {entry["Count"]} times.")

def sort_on(dict):
    return dict["Count"]