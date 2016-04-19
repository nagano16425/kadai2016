import sys
import nltk

if __name__=="__main__":

    # ファイルの読み込み
    f = open (sys.argv[1], "r")
    txt = f.read()
    f.close()

    # NLTKの文分割
    sentences = nltk.tokenize.sent_tokenize( txt.strip() )
    # NLTKの単語分割(最初の文のみ)
    words = nltk.tokenize.word_tokenize( sentences[0] )

    # NLTKのチャンクタガー
    chunk = nltk.tag.SennaChunkTagger('/usr/share/senna-v2.0')
    #  1行1チャンクの出力
    for word in chunk.tag(words):
        # "B-"と"I-"の場合のみ出力
        if not "'" in word[0]:
            if "B-" in word[1]:
                print (word[0]+ " " +(word[1]))
            if "I-" in word[1]:
                print (word[0]+ " " +(word[1]))
