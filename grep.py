import sys   # 標準ライブラリをインポート

if __name__ == "__main__":

    param = sys.argv

    f = open (param[1], "r", encoding="utf-8")
    g = open ("[Grep]" + param[1], "w", encoding="utf-8")
    for line in f:   # ファイルから1行ずつ読み込む
        if " " + param[2] + " "  in line:    # 指定した文字列を検索する
            print(line, end="\n")   # 1行ずつ表示する
            g.write ( line )   # ファイルに書き込む
    g.close()   # ファイルを閉じる
