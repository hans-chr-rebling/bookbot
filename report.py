from file import File

class Report:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = File(file_path)

    def sort_on(self, dict):
        return dict["num"]

    def print(self):
        char_dict = {}
        book_text = self.file.read()
        words = book_text.split()
        report = f"--- Begin report of {self.file_path} ---\n"
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
        results.sort(reverse=True, key=self.sort_on)

        for result in results:
            report += f"The '{result["name"]}' character was found {result["num"]} times\n"
        report += "--- End report ---"

        print(report)    