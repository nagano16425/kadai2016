import sys       # 標準ライブラリをインポート 

if __name__=="__main__":

    param = sys.argv

    f = open (param[1], "r", encoding="utf-8")
    g = open ("[top10]" + param[1], "w", encoding="utf-8")

    # counting
    wordcount = {}
    for line in f:
        for word in line.split():
            wordcount[word] = wordcount.get(word, 0) + 1

    # sort by count
    d = [(v,k) for k,v in wordcount.items()]
    d.sort()      # ソート
    d.reverse()   # 逆順
    for count, word in d[:10]:   # 上位10件を表示
        count = str(count)       # カウント数を文字列に変換
        g.write ( "     " + count ) # カウント数を記入
        g.write ( " " + word + "\n" )  # 単語を記入

    # file close
    f.close()     # ファイルを閉じる
    g.close()     # ファイルを閉じる
