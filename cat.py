import sys    # 標準ライブラリをインポート

if __name__ == "__main__":    # if文のブロック(スクリプトファイルとして実行された場合)

    param = sys.argv

    f = open (param[1], "r", encoding="utf-8")
    for line in f:
        print(line, end=" ")
