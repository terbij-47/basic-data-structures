class WordsFinder:

    def __init__(self, *files : str) -> None:
        self.file_names = files

    def get_all_words(self) -> dict:
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = file.read().lower()
                data = data.replace(',', '').replace('.', '').replace('=', ''). \
                    replace('!', '').replace('?', '').replace(';', ''). \
                    replace(':', '').replace(' - ', '').replace('\n', ' ')
                words = []
                for word in data.split(' '):
                    if word:
                        words.append(word)
                all_words[file_name] = words
        return all_words

    def find(self, word : str) -> dict:
        word = word.lower()
        data = self.get_all_words()
        res = {}
        for file_name, words in data.items():
            if word in words:
                res[file_name] = words.index(word) + 1
        return res

    def count(self, word : str) -> dict:
        word = word.lower()
        data = self.get_all_words()
        res = {}
        for file_name, words in data.items():
            if word in words:
                res[file_name] = words.count(word)
        return res


finder1 = WordsFinder('mother.txt', 'if.txt', 'captain.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
