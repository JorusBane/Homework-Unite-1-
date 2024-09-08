class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = []
        for i in file_name:
            self.file_name.append(i)
    def get_all_words(self):
        dict_of_word = {}
        file_att = ""
        for i in self.file_name:
            with (open(i, encoding = 'utf-8') as file):
                file_att = ""
                for j in file:
                    file_att += j
                for punctuation in [',', '.', '=', '!', '?' ';', ':', '\n']:
                    file_att = file_att.replace(punctuation, " ")
                file_att = file_att.lower()
                dict_of_word.update({i:file_att.split()})
        return dict_of_word
    def find(self, word):
        find_dict = {}
        word = word.lower()
        counter = 1
        for i, j in self.get_all_words().items():
            if word in j:
                for _ in j:
                    if _ == word:
                        break
                    counter += 1
                find_dict.update({i: counter})
        return find_dict
    def count(self, word):
        count_dict = {}
        word = word.lower()
        counter = 0
        for i, j in self.get_all_words().items():
            if word in j:
                for _ in j:
                    if _ == word:
                        counter += 1
                count_dict.update({i: counter})
        return count_dict



finder2 = WordsFinder('test_file.txt', '../test_file1.txt')
for _ in finder2.file_name:
    print(_)
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))