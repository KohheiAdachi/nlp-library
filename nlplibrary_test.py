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

        
if __name__ == '__main__':
    unittest.main()