def main():
    print_report("books/frankenstein.txt")

def read_file(file_path):
    file_contents = ""
    try:
        with open(file_path) as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"ERROR: file:{file_path} not found!")    
    return file_contents

def sort_on(dict):
    return dict["num"]

def print_report(file_path):
    char_dict = {}
    book_text = read_file(file_path)
    words = book_text.split()
    report = f"--- Begin report of {file_path} ---\n"
    report += f"{len(words)} words found in the document\n\n"

    for word in words:
        for char in word:
            char_lower_case = char.lower()
            if char_lower_case.isalpha():
                if char_lower_case not in char_dict:
                    char_dict[char_lower_case] = 1
                else:    
                    char_dict[char_lower_case] += 1    
    
    results = [{"name": key, "num": value} for key, value in char_dict.items()]
    results.sort(reverse=True, key=sort_on)

    for result in results:
        report += f"The '{result["name"]}' character was found {result["num"]} times\n"
    report += "--- End report ---"

    print(report)


main()