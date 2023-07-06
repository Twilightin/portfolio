import pandas as pd
import streamlit as st
from PIL import Image

from annotated_text import annotated_text
from streamlit_extras.colored_header import colored_header

def header(url):
     st.markdown(f'<p style="background-color:#0066cc;color:grey;font-size:20px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

# header("notice")

with st.sidebar:
  st.title('郭 熾辰')
  st.header("Chishin Kaku")
  st.write('A passionate data scientist')

url01 = 'https://twilightin-titanicpred-app-titanicpred-app-48ml2g.streamlit.app/'
url02 = 'https://twilightin-topnews-app-topnews-app-nmz8mo.streamlit.app/'
url03 = 'https://twilightin-plotlyanime-app-plotlyanime-app-kpw3se.streamlit.app/'
url04 = 'https://twilightin-visionalist-covracebar-appcovracebar-app-hss31w.streamlit.app/'
url05 = 'https://twilightin-covview-app-covview-app-wf3ten.streamlit.app/'
url06 = 'https://twilightin-covdl-app-covdl-app-7xzhq6.streamlit.app/'
url07 = 'https://twilightin-app-apigpt-app-apigpt-4plb8a.streamlit.app/'

image01 = Image.open('port01.png')
image02 = Image.open('port02.jpg')
image03 = Image.open('port03.png')
image04 = Image.open('port04.jpg')
image05 = Image.open('port05.jpg')
image06 = Image.open('port06.jpg')
image07 = Image.open('port07.jpg')

video_file01 = open('app01.mp4', 'rb')
video_bytes01 = video_file01.read()

video_file02 = open('app02.mp4', 'rb')
video_bytes02 = video_file02.read()

video_file03 = open('app03.mp4', 'rb')
video_bytes03 = video_file03.read()

video_file04 = open('app04.mp4', 'rb')
video_bytes04 = video_file04.read()

video_file05 = open('app05.mp4', 'rb')
video_bytes05 = video_file05.read()

video_file06 = open('app06.mp4', 'rb')
video_bytes06 = video_file06.read()

video_file07 = open('app07.mp4', 'rb')
video_bytes07 = video_file07.read()

tab1, tab2 = st.tabs(["Data Science", "AI Generated Content（AIGC）"])

with tab1:
          
     #step.2 output new
     
     #columns

     col1, col2 = st.columns(2)

     with col1:
         # 01
          with st.container():
              st.markdown("入力データに応じてモデル(Xgboost)予測の結果とSHAPによるモデルの解釈")
              annotated_text(('機械学習', 'カテゴリ', "#8ef"))
              st.markdown('[リンク先](%s)' % url01)
              with st.expander("デモンストレーション(30s)"):
                  st.write('A simple video demo created by myself.')
                  st.video(video_bytes01)
              st.image(image01)
     
     with col2:
         # 02
          with st.container():         
              st.markdown("各メディアのTOPニュース(URL含め)のまとめサイト                  ")
              annotated_text(('スクレイピング', 'カテゴリ', "#faa"))
              st.markdown("[リンク先](%s)" % url02)
              with st.expander("デモンストレーション(10s)"):
                  st.write('A simple video demo created by myself.')
                  st.video(video_bytes02)
              st.image(image02)
     st.markdown("""---""")
          
     col3, col4 = st.columns(2)

     with col3:
         # 03
         st.markdown("各国GDPと平均寿命の相関を時系列で動的な可視化                      ")
         annotated_text(('データ可視化', 'カテゴリ', '#afa'))
         st.markdown("[リンク先](%s)" % url03)
         with st.expander("デモンストレーション(10s)"):
             st.write('A simple video demo created by myself.')
             st.video(video_bytes03)
         st.image(image03)

     with col4:    
         # 04
         st.markdown("各国のコロナ新規感染者の推移を動的な可視化                                 ")
         annotated_text(('データ可視化', 'カテゴリ', '#afa'))
         st.markdown("[リンク先](%s)" % url04)
         with st.expander("デモンストレーション(10s)"):
             st.write('A simple video demo created by myself.')
             st.video(video_bytes04)
         st.image(image04)
     st.markdown("""---""")
     
     col5, col6 = st.columns(2)

     with col5:
         # 05
         st.markdown("国別のコロナ新規感染者・死亡者の推移と累計                                   ")
         annotated_text(('データ可視化', 'カテゴリ', '#afa'))
         st.markdown("[リンク先](%s)" % url05)
         with st.expander("デモンストレーション(10s)"):
             st.write('A simple video demo created by myself.')
             st.video(video_bytes05)
         st.image(image05)

     with col6:         
        # 06
         st.markdown("特定国/地域データの抽出とダウンロードアプリ                            ")
         annotated_text(('データ可視化', 'カテゴリ', '#afa'))
         st.markdown("[リンク先](%s)" % url06)
         with st.expander("デモンストレーション(10s)"):
             st.write('A simple video demo created by myself.')
             st.video(video_bytes06)
         st.image(image06)
     st.markdown("""---""")
     
     col7, col8 = st.columns(2)

     with col7:
         # 07
         st.markdown("ChatGPT(GPT3.5)より自分用の高度なChatGPT(text-davinci-003のAPI利用)構築")
         annotated_text(('API活用', 'カテゴリ', "#fea"))
         st.markdown("[リンク先](%s)" % url07)
         with st.expander("デモンストレーション(10s)"):
             st.write('A simple video demo created by myself.')
             st.video(video_bytes07)
         st.image(image07)

          
     st.markdown("""---""")
