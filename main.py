def main():
    book_text = read_file("frankenstein.txt")
    print(count_words(book_text))

def read_file(file_name):
    file_path = "books/"
    file_contents = ""
    try:
        with open(file_path+file_name) as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"ERROR: file:{file_name} not found!")    
    return file_contents

def count_words(text):
    return len(text.split())

main()