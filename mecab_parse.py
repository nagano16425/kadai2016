import sys    # System
import MeCab  # MeCab

if __name__=="__main__":

    mecab = MeCab.Tagger("-Ochasen")                  # めかぶ起動
    sent = mecab.parse("「豊工に行っています。」")    # 形態素解析用の文章を入力
    print (sent)
