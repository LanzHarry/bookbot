def count_words(text_input):
    return len(text_input.split())

def count_chars(text_input):
    char_dict = {}
    
    for character in text_input:
        lower_char = character.lower()
        
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1
    
    return char_dict

def sort_on(items):
    return items["num"]

def sort_by_char_count(char_dict):
    char_dict_list = [{"char": k, "num": v} for k, v in char_dict.items()]
    
    char_dict_list.sort(reverse=True, key=sort_on)
    
    return char_dict_list