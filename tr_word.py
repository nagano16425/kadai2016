import sys   # 標準ライブラリをインポート

if __name__=="__main__":

    param = sys.argv

    f = open (param[1], "r", encoding="utf-8")
    g = open ("[tr-word]" + param[1], "w", encoding="utf-8")

    for line in f:
        line = line.split()   # 文字列に含まれている単語をリストに格納する
        line = "\n".join(line)    # リストに格納されている文字列に改行を挿入して戻す
        line = line.strip()   # 空白文字を除去する
        g.write ( line + "\n" )   # ファイルに書き込む

    g.close()   # ファイルを閉じる    
