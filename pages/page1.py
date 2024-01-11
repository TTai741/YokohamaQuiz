import streamlit as st
from PIL import Image #画像用

with st.form(key="profile_form"): #これがあることでボタンが押されないと画面がリロードされない
    point = 0
    st.title("横浜クイズ 観光編")
    
    #テキスト
    st.subheader("Q1. この画像は、どこで撮影されたでしょうか？")
    #画像
    Image_Q1 = Image.open("./datas/山下公園.jpg")
    st.image(Image_Q1,width=500)
    #ラジオボタン
    category1 = st.radio("４択",("A:横浜中華街","B:横浜赤レンガ倉庫","C:山下公園","D:横浜・八景島シーパラダイス"))

    st.subheader("Q2. この画像は、何という建物でしょうか？")
    Image_Q2 = Image.open("./datas/横浜市開港記念会館.jpg")
    st.image(Image_Q2,width=500)
    category2 = st.radio("４択",("A:横浜市開港記念会館","B:横浜市歴史博物館","C:横浜市立美術館","D:横浜市民ギャラリー"))
    
    st.subheader("Q3. この画像は、何という施設でしょうか？")
    st.image("https://cdn-ak.f.st-hatena.com/images/fotolife/t/travelyokohama/20200630/20200630125608.jpg",width=500)
    category3 = st.radio("４択",("A. カップヌードルミュージアム横浜","B. 新横浜ラーメン博物館","C. 三菱みなとみらい技術館","D. キリンビール横浜工場"))
    
    st.subheader("Q4. この画像は、何というアトラクションでしょうか？")
    st.image("https://www.coastergallery.com/japan/Surf_Coaster_Leviathan-23.jpg",width=500)
    category4 = st.radio("４択",("A. サーフコースターリヴァイアサン","B. バンジージャンプ","C. コスモクロック21","D. メリーゴーラウンド"))
    
    st.subheader("Q5. この画像は、何という公園でしょうか？")
    st.image("https://stat.ameba.jp/user_images/20161027/23/ayha0731/cb/9f/j/o2560192013783534606.jpg",width=500)
    category5 = st.radio("４択",("A. 三溪園","B. こどもの国","C. 港の見える丘公園","D. 野毛山公園"))
    
    st.subheader("Q6. この画像は、何というホールでしょうか？")
    st.image("https://travel.navitime.com/ja/m/kanko/wp-content/uploads/article_paragraph_dir/330/body_1.jpg?t=",width=500)
    category6 = st.radio("４択",("A. 横浜アリーナ","B. 神奈川県民ホール","C. 横浜ランドマークホール","D. 横浜ベイホール"))
    
    st.subheader("Q7. この画像は、何という橋でしょうか？")
    st.image("https://static.retrip.jp/article/4578/images/4578f5587bbf-5368-4d48-aeaf-48c189493af7_l.jpg",width=500)
    category7 = st.radio("４択",("A. 横浜ベイブリッジ","B. 大さん橋","C. 関内大橋","D. 本牧大橋"))
    
    st.subheader("Q8. この画像は、何というタワーでしょうか？")
    st.image("https://skyticket.jp/guide/wp-content/uploads/pixta_42008201_M.jpg",width=500)
    category8 = st.radio("４択",("A. 横浜マリンタワー","B. 横浜ランドマークタワー","C. 横浜ロイヤルパークホテル","D. 横浜ポートタワー"))
    
    st.subheader("Q9. この画像は、何という温泉施設でしょうか？")
    st.image("https://sp.jorudan.co.jp/onsen/images/spot/640/284_1.jpg",width=500)
    category9 = st.radio("４択",("A. 横浜みなとみらい 万葉倶楽部","B. 横浜天然温泉 スパエトワール","C. 横浜湯の町温泉","D. 横浜元町温泉"))
    
    st.subheader("Q10. この画像は、何という動物園でしょうか？")
    st.image("https://www.zoochat.com/community/media/oklahoma-city-zoo-2010-okapi.130543/full?d=1292515532",width=500)
    category10 = st.radio("４択",("A. 野毛山動物園","B. こども動物園","C. よこはま動物園ズーラシア","D. 横浜・八景島シーパラダイス"))
    
    
    #ボタン
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")
    
    
    if submit_btn:
        
        if category1 == "C:山下公園":
            st.text("Q1正解!!")
            point += 1
        else:
            st.text("Q1不正解!! 正解はC:山下公園")
        if category2 == "A:横浜市開港記念会館":
            st.text("Q2正解!!")
            point += 1
        else:
            st.text("Q2不正解!! 正解はA:横浜市開港記念会館")
        if category3 == "A. カップヌードルミュージアム横浜":
            st.text("Q3正解!!")
            point += 1
        else:
            st.text("Q3不正解!! 正解はA. カップヌードルミュージアム横浜")
        if category4 == "A. サーフコースターリヴァイアサン":
            st.text("Q4正解!!")
            point += 1
        else:
            st.text("Q4不正解!! 正解は A. サーフコースターリヴァイアサン")
        if category5 == "C. 港の見える丘公園":
            st.text("Q5正解!!")
            point += 1
        else:
            st.text("Q5不正解!! 正解は C. 港の見える丘公園")
        if category6 == "A. 横浜アリーナ":
            st.text("Q6正解!!")
            point += 1
        else:
            st.text("Q6不正解!! 正解はA. 横浜アリーナ")
        if category7 == "A. 横浜ベイブリッジ":
            st.text("Q7正解!!")
            point += 1
        else:
            st.text("Q7不正解!! 正解は A. 横浜ベイブリッジ")
        if category8 == "B. 横浜ランドマークタワー":
            st.text("Q8正解!!")
            point += 1
        else:
            st.text("Q8不正解!! 正解は B. 横浜ランドマークタワー")
        if category9 == "A. 横浜みなとみらい 万葉倶楽部":
            st.text("Q9正解!!")
            point += 1
        else:
            st.text("Q9不正解!! 正解はA. 横浜みなとみらい 万葉倶楽部")
        if category10 == "C. よこはま動物園ズーラシア":
            st.text("Q10正解!!")
            point += 1
        else:
            st.text("Q10不正解!! 正解はC. よこはま動物園ズーラシア")
            
            
        
        
        st.text(f"{point}/10点です")
        if point == 10:
            st.text("全問正解!! 横浜マスター!!")