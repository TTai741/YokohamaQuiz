import streamlit as st



with st.form(key="histry_form"): #これがあることでボタンが押されないと画面がリロードされない
    point_h = 0
    st.title("横浜クイズ 歴史＆地理編")
    
    #テキスト
    st.subheader("問題１：横浜が開港したのは西暦何年でしょうか？")
    #画像
    st.image("https://www.yokohamaport.co.jp/wp/wp-content/uploads/2022/03/yokohamakou-R2-PA-01.jpg",width=500)
    #ラジオボタン
    h_category1 = st.radio("４択",("a) 1854年","b) 1858年","c) 1859年","d) 1868年"))

    st.subheader("問題２：横浜に市制がしかれたのは明治何年でしょうか？ (2点問題)")
    h_category2 = st.slider("明治",min_value=1,max_value=45)
    
    st.subheader("問題３：横浜市の市歌は開港何周年記念祭のときに制定されたでしょうか？")
    st.image("https://stat.ameba.jp/user_images/20180915/00/mlb29900/cb/e5/j/o1080063514266089055.jpg",width=500)
    h_category3 = st.selectbox("４択",("a) 25周年","b) 50周年","c) 75周年","d) 100周年"))
    
    st.subheader("問題４：横浜市の市花は何でしょうか？")
    h_category4 = st.selectbox("４択",("a) 椿","b) 桜","c) バラ","d) ツツジ"))
    
    st.subheader("問題５：横浜市の区の数はいくつでしょうか？")
    st.image("https://www.travel-zentech.jp/japan/kanagawa/img/Map_of_Yokohama_City_480x640.png",width=500)
    h_category5 = st.slider("区の数",min_value=0,max_value=47)
    
    st.subheader("問題６：横浜市の最も人口の多い区はどこでしょうか？ (2点問題)")
    h_category6 = st.text_input("区の名前")
    
    st.subheader("問題７：日本の公園の発祥地は横浜ですが、１８７０年に開設された発祥の始まりとなった公園は？ (2点問題)")
    h_category7 = st.text_input("公園の名前")
    


    
    #ボタン
    submit_btn_histry = st.form_submit_button("送信")
    cancel_btn_histry = st.form_submit_button("キャンセル")
    
    
    if submit_btn_histry:
        
        if h_category1 == "c) 1859年":
            st.text("問題１ 正解!!")
            point_h += 1
        else:
            st.text("問題１ 不正解!! 正解はc) 1859年")
        if h_category2 == 22:
            st.text("問題２ 正解!!")
            point_h += 2
        else:
            st.text("問題２ 不正解!! 正解は22")
        if h_category3 == "b) 50周年":
            st.text("問題３ 正解!!")
            point_h += 1
        else:
            st.text("問題３ 不正解!! 正解はb) 50周年")
        if h_category4 == "c) バラ":
            st.text("問題４ 正解!!")
            point_h += 1
        else:
            st.text("問題４ 不正解!! 正解はc) バラ")
        if h_category5 == 18:
            st.text("問題５ 正解!!")
            point_h += 1
        else:
            st.text("問題５ 不正解!! 正解は18")
        if h_category6 == "港北区":
            st.text("問題６ 正解!!")
            point_h += 2
        else:
            st.text("問題６ 不正解!! 正解は港北区")
        if h_category7 == "山手公園":
            st.text("問題７ 正解!!")
            point_h += 2
        else:
            st.text("問題７ 不正解!! 正解は山手公園")
        
        st.text(f"{point_h}/10点です")
        if point_h == 10:
            st.text("全問正解!! 横浜マスター!!")
            