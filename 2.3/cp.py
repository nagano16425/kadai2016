import sys    # 標準ライブラリをインポート

if __name__ == "__main__":

    param = sys.argv

    f = open (param[1], "r", encoding="utf-8")
    s = f.read()   # ファイルを読み込む
    f.close()   # ファイルを閉じる

    g = open ("[Copy]" + param[1], "w", encoding="utf-8")
    g.write( s )   # ファイルに書き込む
    g.close()   # ファイルを閉じる
