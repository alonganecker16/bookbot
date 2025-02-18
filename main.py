def print_report(dict):
    for char in dict:
        if char.isalpha():
            print(f"The '{char}' character was found {dict[char]} times")

def char_count(text):
    lowered_text = text.lower()
    chars = list(lowered_text)
    char_count_dict = {}

    for char in chars:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    
    return char_count_dict

def word_count(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(word_count(file_contents))
        char_dict = char_count(file_contents)
        # print(char_dict)
        print_report(char_dict)


if __name__ == '__main__':
    main()