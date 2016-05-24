import CaboCha  # CaboCha

if __name__=="__main__":

    c = CaboCha.Parser('--charset=UTF8')           # 構文解析ツール(CaboCha)をUTF-8で使う
    sentence = "「豊工に行っています。」"          # 解析用の文を入力
    tree =  c.parse(sentence)                      # 解析用の文を構文解析ツール(CaboCha)へ送る
    print (tree.toString(CaboCha.FORMAT_LATTICE))  # 出力
