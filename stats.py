def word_count(book_text):
    count = 0
    text = book_text.split()
    for words in text:
        count += 1
    
    return count

def character_count(text):

    char_count = {}

    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_characters_by_count(char_dict):
    """
    Takes a dictionary of characters and their counts, sorts them
    from greatest to least by count, and outputs in the desired format.
    """
    # Convert the dictionary into a list of tuples (character, count)
    char_list = list(char_dict.items())
    sorted_list = []
    
    # Define a function to extract the count
    def get_count(item):
        return item[1]
    
    # Sort the list by using the 'get_count' function as the key
    char_list.sort(key=get_count, reverse=True)
    
    # Format and print the output
    for char, count in char_list:
        sorted_list.append(f"{char}: {count}")
    
    return sorted_list