def read_book():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents
        
def character_count(file_contents):
    res = dict()
    file_contents = file_contents.lower()
    chars = set(file_contents)
    for letter in chars:
        letter_count = file_contents.count(letter)
        res[letter] = letter_count
    return res

def count_words(file_contents):
    count = len(file_contents.split())
    return count

def main():    
    book = read_book()
    n_words = count_words(book)
    count_chars = character_count(book)
    dict_sorted = dict(sorted(count_chars.items(), key=lambda item: item[1], reverse=True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f" \{n_words} words found in the document")
    for value in dict_sorted:
        if value == '\n':
            print(f"The \\n character was found {dict_sorted[value]} times")
        else:
            print(f"The {value} character was found {dict_sorted[value]} times")
    print("--- End report ---")
main()