# coding: utf-8
import sys
import nltk
import gzip
import MeCab
import shelve

def sent_tokenize(review):
    jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')   # 日本語の文分割用のTokenizer
    sents = jp_sent_tokenizer.tokenize(review.strip('\n'))
    return sents

def to_fv(review):
    mecab = MeCab.Tagger("-Ochasen")          # ChaSen互換形式
    mecab.parse(" ")                          # UnicodeDecodeError回避(MeCabとPython3のバグ回避)
    for sent in sent_tokenize(review):
        sent = sent.strip('\n')
        node = mecab.parseToNode(sent)        # 形態素の詳細情報のノードを取得
        node = node.next                      # コールバック関数
        while node:
            word = node.surface               # 表層
            if word not in index:
                index[word] = len(index) + 1  # increment index
                count[ index[word] ] = 1      # count initialize
            else:
                count[ index[word] ] += 1     # increment count
                node = node.next              # コールバック関数
    return

if __name__=="__main__":
    
    f = gzip.open(sys.argv[1], "rt")          # gzip形式のファイルを開く
    reviews = f.readlines()                   # ファイルを全て読み込み、1行毎に処理を行う
    f.close()

    # shelve
    sh = shelve.open("index.shelve")
    sh = {}                       
    sh["count"] = {}
    sh["word"] = {}
    index = sh["word"]
    count = sh["count"]

    for review in reviews:
        review = review.strip('\n')
        to_fv(review)
    print (sh["word"])
