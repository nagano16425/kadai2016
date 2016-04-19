# ディレクトリ内のファイルを読み込んで、行の先頭に指定したラベルを追加

import sys
import nltk      # NLTK module
import shelve    # Shelve module
import os        # OS module

if __name__=="__main__":

    # get directry name
    fs = os.listdir (sys.argv[1])
    
    # make output file
    g = open (sys.argv[2], "w")
    
    # read each files
    for fn in fs:
        f = open (sys.argv[1] + "/" + fn, "r", encoding="utf-8")
        txt = f.read()
        f.close()

        # NLTK word segmentation with counting
        wordcount = {}
        # shelve
        sh = shelve.open("index.shelve")

        # Processing
        for line in nltk.tokenize.sent_tokenize(txt.strip()):
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

        label = []
        label.append(str(sys.argv[3]))           # Import label
            
        # sort by count
        for k,v in sorted(wordcount.items(), key = lambda x:int(x[0])):            
            k = str(k)    # インデックスの頻度を文字列に変換
            v = str(v)    # インデックス順を文字列に変換
            label.append ( k + ":" + v + "\t" )    # カウント数を記入
        g.write ( " ".join(label) + "\n" )
        # g.write( txt )
    g.close()    # ファイルを閉じる
