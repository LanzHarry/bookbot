from stats import(
    count_words, 
    count_chars, 
    sort_by_char_count
    )
import sys


def get_book_text(file_path):
    file_text_content = None
    
    with open(file_path) as f:
        file_text_content = f.read()
    
    return file_text_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_chars = count_chars(book_text)
    char_count_list = sort_by_char_count(num_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for elt in char_count_list:
        if elt["char"].isalpha():
            print(f"{elt["char"]}: {elt["num"]}")
    print("============= END ===============")
    

if __name__ == "__main__":
    main()