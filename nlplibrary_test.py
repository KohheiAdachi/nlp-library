# -*- coding:utf-8 -*-


import unittest
import nlplibrary as nlp

class Testnlplibrary(unittest.TestCase):
    def test_tokenize(self):
        text = "今日はいい天気ですね"
        print(nlp.tokenize(text))
    
    def test_tokenize_all(self):
        text = "今日はいい天気ですね"
        print(nlp.tokenize_all(text))
 
    def test_read_doc(self):
        print(nlp.read_doc("test.txt"))

    def test_extract_noun(self):
        print(nlp.extract_noun("今日はいい天気"))
        
if __name__ == '__main__':
    unittest.main()