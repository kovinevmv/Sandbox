import requests, string, re, jamspell 
from nltk.tokenize import word_tokenize
from text_extractor import *

DICT_PATH = '/home/alien/Desktop/git/Sandbox/Scripts/spell_checker/ru_small.bin'
russian_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

class TextProcessor:
    def __init__(self, url, type_extraction='raw'):
        self.punctuation_re = re.compile(f'[{re.escape(string.punctuation)}]')
        self.digits_re = re.compile(r'\d+')
        self.no_words_re = re.compile(r'\W+')

        self.url = url
        self.content = self.get_html(self.url)
        self.words = self.extract_text_from_html(self.content, type_extraction)
        self.russian_words = self.extract_russian_words(self.words)

    
    def get_html(self, url):
        return requests.get(url).text

    def extract_text_from_html(self, page, type_extraction):
        if type_extraction == 'bs4':
            text = BS4_HTMLToTextConverter(page).get_text()
        elif type_extraction == 'h2t':
            text = html2text_HTMLToTextConverter(page).get_text()
        elif type_extraction == 'raw':
            text = raw_HTMLToTextConverter(page).get_text()
        else:
            text = BS4_HTMLToTextConverter(page).get_text() + html2text_HTMLToTextConverter(page).get_text() + raw_HTMLToTextConverter(page).get_text()

        return list(set(self.word_breaking(text)))
        
    def word_breaking(self, text):
        clean_text = self.punctuation_re.sub(' ', text)
        clean_text = self.digits_re.sub(' ', clean_text)
        clean_text = self.no_words_re.sub(' ', clean_text)

        return word_tokenize(clean_text)

    def extract_russian_words(self, words):
        regex = re.compile(f'[{russian_chars}]')
        return list(filter(lambda word: re.findall(regex, word), words))

    def validate_words(self, words=None):
        if not words:
            words = self.russian_words
        
        corrector = jamspell.TSpellCorrector()
        corrector.LoadLangModel(DICT_PATH)

        detected_errors = []
        for word in words:
            correct = corrector.FixFragment(word)
            if correct != word:
                detected_errors.append((word, correct))

        return detected_errors
                
    def get_words(self):
        return self.russian_words


example_url = 'https://github.com/SqrtMinusOne/conspect/blob/master/src/%D0%A1%D0%B5%D0%BC_7/%D0%91%D0%96%D0%94/conspect.tex'

t = TextProcessor(example_url, type_extraction='all')
errors = t.validate_words()
for (word, correct) in errors:
    print(f"'{word}' --- fix ---> '{correct}'")