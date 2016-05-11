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

def mecab_parse(review):
    mecab = MeCab.Tagger("-Ochasen")          # ChaSen互換形式
    mecab.parse(" ")                          # UnicodeDecodeError回避(MeCabとPython3のバグ回避)
    for sent in sent_tokenize(review):
        sent = sent.strip('\n')
        node = mecab.parseToNode(sent)        # 形態素の詳細情報のノードを取得
        # surface
        word = []                             # 表層(単語)を格納する配列
        while node:          
            word = node.surface               # 表層
            if word not in index:
                index[word] = len(index) + 1  # increment index
                count[ index[word] ] = 1      # count initialize
            else:
                count[ index[word] ] += 1     # increment count
                node = node.next              # コールバック関数
        # N-gram
        sentence=[]
        for i in range(len(word)):
            if (i != len(word)-1):
                if (n == "2"):
                    sentence.append(str(word[i])+str(word[i+1]))
                if (n == "3") and (i != len(wordList)-2):
                    sentence.append(str(word[i])+str(word[i+1])+str(word[i+2]))
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

    # N-gram
    n = sys.argv[2]

    for review in reviews:
        review = review.strip('\n')           # 不要な空白,改行を削除
        mecab_parse(review)
    print (sh["count"])                       # 素性ベクトルを出力
