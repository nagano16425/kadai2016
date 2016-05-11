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
        node = node.next                      # コールバック関数
        while node:
            word = node.surface               # 表層
            array = node.feature.split(",")   # 品詞を分割
            for i in range(4):
                pos.insert(i, array[i])       # 品詞(pos[0]～pos[3])
            if pos[0] in {u"名詞",u"動詞",u"形容詞",u"形容動詞",u"副詞"}:
                # print ( word,pos[0] )       # 内容語(名詞,動詞,形容詞,形容動詞,副詞)判定確認用
                node = node.next              # コールバック関数
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

    # feature
    pos = []                                  # 品詞を格納する配列

    for review in reviews:
        review = review.strip('\n')           # 不要な空白,改行を削除
        mecab_parse(review)
    print (sh["count"])                       # 素性ベクトルを出力
