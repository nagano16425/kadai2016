# coding: utf-8
import sys
import nltk
import gzip

if __name__=="__main__":
    jp_sent_tokenizer = nltk.RegexpTokenizer(u'[^！？。]*[！？。]?')   # 日本語の文分割用のTokenizer
    f = gzip.open(sys.argv[1], "rt")                                   # gzip形式のファイルを開く
    reviews = f.readlines()                                            # ファイルを全て読み込み、1行毎に処理を行う
    i = 0                                                              # レビューの先頭を"0"とする
    for review in reviews:
        if i >= 1:                                                     # 文分割するレビュー数を超えた場合
            break                                                      # ループ終了
        sents = jp_sent_tokenizer.tokenize(review.strip('\n'))         
        j = 1
        sent_num = int(len(sents))                                     # 一つのレビューに対して文の数を定義する
        for sent in sents:                                             # 対象レビューに対して文分割を実施
            sent = sent.strip('\n')
            if sent_num == j:                                          # 対象レビューの 最後の文の時
                print (sent)                                           
            else:                                                      
                print (sent)
            j += 1
        i += 1
