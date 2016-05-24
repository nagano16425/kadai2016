import sys
import nltk

if __name__=="__main__":

    f = open (sys.argv[1], "r")
    txt = f.read()
    f.close()

    # NLTKの文分割
    sentence = nltk.tokenize.sent_tokenize( txt )
    for line in sentence:
　　　　# NLTKの単語分割
        line = nltk.tokenize.word_tokenize( line )
        for word in line:
            print ( word )
