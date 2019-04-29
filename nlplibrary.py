# -*- coding:utf-8 -*-

import MeCab


def tokenize(doc):
    """形態素解析し，指定した品詞の単語リストを返す
    Parameters
    -------
    doc:str
        文字列
    Returns
    -----
    words:list
        形態素解析後のリスト
    """
    mecab = MeCab.Tagger("-Ochasen")
    lines = mecab.parse(doc).splitlines()
    words = []
    stop_words = []
    for line in lines:
        chunks = line.split('\t')
        if len(chunks) > 3 and not chunks[2] in stop_words:
            if chunks[3].startswith('動詞'):
                words.append(chunks[2])
            if chunks[3].startswith('名詞') and not chunks[0] in stop_words:
                words.append(chunks[0])
            if chunks[3].startswith('副詞'):
                words.append(chunks[0])
            if chunks[3].startswith('感動詞'):
                words.append(chunks[0])
            if chunks[3].startswith('形容詞'):
                words.append(chunks[2])
            if chunks[3].startswith('形容動詞'):
                words.append(chunks[2])    
    return words

def tokenize_all(doc):
    """形態素解析をすべて単語が含まれているリストを返す
    Parameters
    -------
    doc:str
        文字列
    Returns:list
        単語リスト
    """
    mecab = MeCab.Tagger("-Ochasen")
    lines = mecab.parse(doc).splitlines()
    words = []
    stop_words = []
    for line in lines:
        chunks = line.split('\t')
        if not chunks[0] in stop_words:
            words.append(chunks[0])
    words.remove("EOS")
    return words
           
        