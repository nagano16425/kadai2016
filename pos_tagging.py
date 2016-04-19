import sys
import nltk

if __name__=="__main__":

    # ファイルの読み込み
    f = open (sys.argv[1], "r")
    txt = f.read()
    f.close()
    
    # NLTKの文分割
    sentences = nltk.tokenize.sent_tokenize( txt )
    # NLTKの単語分割
    words = nltk.tokenize.word_tokenize( sentences[0] )

    # NLTKの品詞分割の初期化
    pos = nltk.tag.SennaTagger('/usr/share/senna-v2.0')
    # NLTKの品詞分割
    for word in pos.tag( words ):
        print ( word )
