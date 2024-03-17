def main():
    with open("books/frankenstein.txt") as f: 
        file_contents = f.read()
        return file_contents

def count_words(file_contents):
    words = file_contents.split()
    lenght = len(words)
    return lenght
    
def count_letters(file_contents):
    lowered_string = file_contents.lower()
    entire_letters = {}
    for letter in lowered_string: 
        if letter.isalpha():
            if letter in entire_letters: 
                entire_letters[letter] += 1
            else: 
                entire_letters[letter] = 1
    return entire_letters

def sorting_list(entire_letters):
    converted_list = []
    for char, num in entire_letters.items():
        converted_list.append({"char": char, "num": num})
    converted_list.sort(reverse=True, key=lambda converted_list: converted_list["num"])
    return converted_list

def report(length, converted_list):
    file_book = "books/frankenstein.txt"
    print(f"--- Begin report of {file_book} ---")
    print(f"{length} words found in the document")
    print("")
    for dict in converted_list:
        print(f"The '{dict["char"]}' character was found {dict["num"]} times ")
    print("--- End report ---")

file_contents = main()
length = count_words(file_contents)
entire_letters = count_letters(file_contents)
converted_list = sorting_list(entire_letters)

#print(count_letters(file_contents))
#print(count_words(file_contents))
#print(main()) 
#print(sorting_list(entire_letters))
report(length, converted_list)

main()
