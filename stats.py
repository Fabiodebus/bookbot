def count_words(text):
    num_words = len(text.split())
    return num_words

def count_characters(text):
    characters = {}
    new_text = text.lower()
    for char in new_text:
        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

def sort_characters(characters):
    # Convert dictionary to list of dictionaries with 'character' and 'count' keys
    char_list = []
    for char, count in characters.items():
        char_list.append({'character': char, 'count': count})
    
    # Sort the list by count in descending order (greatest to least)
    sorted_chars = sorted(char_list, key=lambda x: x['count'], reverse=True)
    
    return sorted_chars
    