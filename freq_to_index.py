import sys
import nltk

if __name__=="__main__":

    # ファイルの読み込み
    f = open (sys.argv[1], "r")
    txt = f.read()

    # NLTKのファイルを作成
    g = open ("[top10_in_NLTK]" + sys.argv[1], "w")

    # NLTKの文分割
    sentences = nltk.tokenize.sent_tokenize( txt )
    # NLTKの単語分割 with counting
    wordcount = {}
    # インデックス
    index = {}

    # preprocess
    for line in sentences:
        line = nltk.tokenize.word_tokenize( line )
        for word in line:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1
                index[word] = len(wordcount) +1    # 最初の単語は1とする
            
    # sort by count
    d = [(v,k) for k,v in wordcount.items()]
    d.sort()
    d.reverse()
    for count, word in d[:10]:        # 上位10件を表示
        count = str(count)            # カウント数を文字列に変換
        word = str(word)              # 単語を文字列に変換
        g.write ( str(index[word]) + "\t" )  # インデックスを記入
        g.write ( count + "\t" )    # カウント数を記入
        g.write ( word + "\n" ) # 単語を記入

    f.close()    # ファイルを閉じる
    g.close()    # ファイルを閉じる
