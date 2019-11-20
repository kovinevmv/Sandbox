import requests, string, re, sys, os
from nltk.tokenize import word_tokenize
from pyaspeller import Word
from text_extractor import *
from utils import parse_cookies

DICT_PATH = '/home/alien/Desktop/git/Sandbox/Scripts/spell_checker/ru_small.bin'
russian_chars = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

parsed_cookies = parse_cookies()

punctuation_re = re.compile(f'[{re.escape(string.punctuation)}]')
digits_re = re.compile(r'\d+')
no_words_re = re.compile(r'\W+')

class TextProcessor:
    def __init__(self, url, type_extraction='raw', type_='web'):
        self.punctuation_re = punctuation_re
        self.digits_re = digits_re
        self.no_words_re = no_words_re
        self.cookies = parsed_cookies

        self.file_type = type_

        self.url = url
        self.content = self.get_content(self.url, self.file_type)
        self.words = self.extract_text_from_html(self.content, type_extraction)
        self.russian_words = self.extract_russian_words(self.words)
    
    def get_content(self, link, type_):
        if type_ == 'web':
            return requests.get(link, cookies=self.cookies).text
        if type_ == 'dir':
            with open(link, 'r', errors='ignore') as f:
                output = f.read()
            return output

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
        
        detected_errors = []
        for word in words:
            check = Word(word)
            if not check.correct:
                detected_errors.append((word, ', '.join(check.variants)))

        return detected_errors
                
    def get_words(self):
        return self.russian_words

