
from stats import word_count, character_count, sort_characters_by_count
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    
    if len(sys.argv) < 2:
        print("Required: Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book = (get_book_text(filepath))
    sorted_dict = sort_characters_by_count(character_count(book))

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('----------- Word Count ----------')
    print(f'Found {word_count(book)} total words')

    print('--------- Character Count -------')
   
    for char in sorted_dict:
        if char[0].isalpha():
            print(char)

main()