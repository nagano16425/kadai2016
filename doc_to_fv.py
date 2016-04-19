# bag-of-words(BOW)表現による素性ベクトル(feature vector)

import sys
import nltk      # NLTK
import shelve    # shelve

if __name__=="__main__":

    # ファイルの読み込み
    f = open (sys.argv[1], "r")
    txt = f.read()

    # NLTKのファイルを作成
    g = open ("[FV_NLTK]" + sys.argv[1], "w")

    # NLTKの文分割
    sentences = nltk.tokenize.sent_tokenize( txt.strip() )
    # NLTKの単語分割 with counting
    wordcount = {}
    # shelve
    sh = shelve.open("index.shelve")

    # Processing
    for line in sentences:
        line = nltk.tokenize.word_tokenize( line )
        for word in line:
            indexcount = 0    # index count : インデックスの頻度
            # indexcounter
            if word not in sh:
                indexcount = len(sh) + 1     # increment index
                sh[word] = indexcount
            else:
                indexcount= sh[word]         # put on shelve
            # wordcounter
            if indexcount in wordcount:
                wordcount[indexcount] += 1   # increment count
            else:
                wordcount[indexcount] = 1    # count initialize

    sh.close()    # Close Shelve
            
    # sort by count
    for k,v in sorted(wordcount.items(), key = lambda x:int(x[0])):           
        k = str(k)    # インデックス順を文字列に変換
        v = str(v)    # インデックスの頻度を文字列に変換
        g.write ( k + ":" + v + "\t" )    # カウント数を記入

    g.write( "\n" )   # 改行を挿入

    f.close()    # ファイルを閉じる
    g.close()    # ファイルを閉じる
