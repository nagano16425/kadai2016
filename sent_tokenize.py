import sys     # 標準ライブラリをインポート
import nltk    # NLTKライブラリをインポート
# nltk.download( "punkt" )

if __name__=="__main__":

    f = open (sys.argv[1], "r")
    txt = f.read()    # ファイルを読み込み
    f.close()       # ファイルを閉じる

    sentence = nltk.tokenize.sent_tokenize( txt )
    for line in sentence:
        print ( line +  "\n" )
