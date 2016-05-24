import CaboCha  # CaboCha

if __name__=="__main__":

    c = CaboCha.Parser('-n1')                   # 構文解析ツール(CaboCha)のオプションを指定
    sentence = "「豊工に行っています。」"       # 解析用の文を入力
    tree =  c.parse(sentence)                   # 解析用の文を構文解析ツール(CaboCha)へ送る
    # print (tree.toString(CaboCha.FORMAT_XML)) # 出力

    for i in range(tree.token_size()):
        token = tree.token(i)
        if not token.ne=="O":                   # 固有表現の種別が"O"でない場合
            print ('Surface:', token.surface)   # 表層
            array = token.feature.split(",")    # 素性ベクトルの分解
            print (' Feature:', array[0])       # 素性ベクトル(品詞のみ)
            print (' NE:', token.ne)            # 固有表現
            print ('\t')

# class Material:
        # print (' Feature:', token.feature)              # 素性ベクトル(品詞等)
        # print (' Normalized:', token.normalized_surface)
        # print (' Info:', token.additional_info)
        # print (' Chunk:', token.chunk)
