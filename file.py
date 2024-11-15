class File:
     def __init__(self, file_path):
         self.__file_path = file_path
         
     def read(self):
        file_contents = ""
        try:
            with open(self.__file_path) as file:
                file_contents = file.read()
        except FileNotFoundError:
            print(f"ERROR: file:{self.__file_path} not found!")    
        return file_contents
