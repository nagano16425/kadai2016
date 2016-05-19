# coding: utf-8
from nltk.tokenize import RegexpTokenizer
import sys
import gzip
import MeCab

def unigram(): # 1-gram
    if not node.surface == '':
        n_word = node.surface
        fv(n_word)
    return

def bigram(): # 2-gram
    i=0
    for i in range(len(sentence)-1):
        n_word = sentence[i] + sentence[i+1]
        i += 1
        fv(n_word)
    return

def trigram(): # 3-gram
    i=0
    for i in range(len(sentence)-2):
        n_word = sentence[i] + sentence[i+1] + sentence[i+2]
        i += 1
        fv(n_word)
    return

def fv(n_word): # Feature-vector
    if n_word not in index:
        new_index = len(index) + 1
        index[n_word] = new_index
    if index[n_word] in count:
        count[index[n_word]] += 1
    else:
        count[index[n_word]] = 1
    return

if __name__=="__main__":
    
    # gzip形式のファイルを開き,1行毎に処理を行う
    reviews = gzip.open(sys.argv[1], "rt").readlines()

    # Tokenize&MeCab
    jp_sent_tokenizer = RegexpTokenizer(u'[^！？。]*[！？。]?')   # 日本語の文分割用のTokenizer
    mecab = MeCab.Tagger("-Ochasen")                              # ChaSen互換形式
    mecab.parse(" ")                                              # UnicodeDecodeError回避(MeCabとPython3のバグ回避)

    # Feature-vector
    index = {}
    count = {}

    # N-gram
    n = sys.argv[2]

    # Error message & Exit
    if sys.argv[2] not in ("1","2","3"):
        print("unigram:1,bigram:2,trigram:3")
        sys.exit()

    # Process
    for review in reviews:
        sents = jp_sent_tokenizer.tokenize(review.strip('\n'))    # 不要な空白,改行を削除
        sentence = []                                             # n-gram用の配列
        for sent in sents:
            node = mecab.parseToNode(sent.strip('\n'))            # 形態素の詳細情報のノードを取得
            if (sys.argv[2]=="1"):
                while node:
                    unigram()
                    node = node.next                  
            if (sys.argv[2]=="2"or"3"):
                while node:
                    sentence.append(node.surface)
                    node = node.next
        if (sys.argv[2]=="2"):
            bigram()
        if (sys.argv[2]=="3"):
            trigram()
        
        # output
        for k,v in sorted(count.items(),key=lambda x:int(x[0])):
            print(str(k)+":"+str(v),end=" ")
        print("")

        # Clear
        count={}
