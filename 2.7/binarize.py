import sys

if __name__=="__main__":
    for line in open(sys.argv[1]):    # .txtファイルを各行毎に変換
        label = int(line[0])          # 数値のみラベルとして取り出し
        if label >= 4:                # ラベルが４以上の時
            label = 1                 # 「１」
        else:                         # ラベルが４以上以外の時
            label = -1                # 「-１」
        print (label)                 # 出力
