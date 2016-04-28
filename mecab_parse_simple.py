import sys    # System
import MeCab  # MeCab

if __name__=="__main__":

    mecab = MeCab.Tagger("-Ochasen")          # ChaSen互換形式
    mecab.parse(" ")                          # UnicodeDecodeError回避(MeCabとPython3のバグ回避)
    sentence = ("「豊工に行っています。」")   # 形態素解析用の文章を入力
    node = mecab.parseToNode(sentence)        # 形態素の詳細情報のノードを取得
    node = node.next                          # コールバック関数

while node:
    pos = []                                  # 表層,品詞,原形を格納する配列を用意
    surface = node.surface                    # 表層
    array = node.feature.split(",")           # 品詞,原形を分割
    for i in range(4):
        pos.insert(i, array[i])               # 品詞(pos[0]～pos[3])
    base = array[6]                           # 原形
    print (surface,"\t",pos[0],pos[1],pos[2],pos[3],base)
    node = node.next                          # コールバック関数
