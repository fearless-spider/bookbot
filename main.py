def main():
    with open("books/frankenstein.txt") as f:
        file_content = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_content)} words found in the document\n")
        characters = count_characters(file_content)
        for char in characters:
            print(f"The '{char}' character was found {characters[char]} times")
        print("--- End report ---")

def count_words(content):
    words_list = content.replace('\n', ' ').split(' ')
    new_words_list = []
    for word in words_list:
        if word != '':
            new_words_list.append(word)
    return len(new_words_list)

def count_characters(content):
    result = {}
    for char in content.lower():
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

main()
