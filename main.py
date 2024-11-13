def main():
    print(read_file("frankenstein.txt"))

def read_file(file_name):
    file_path = "books/"
    file_contents = ""
    try:
        with open(file_path+file_name) as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"ERROR: file:{file_name} not found!")    
    return file_contents

main()