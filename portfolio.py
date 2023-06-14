import pandas as pd
import streamlit as st
from annotated_text import annotated_text

def cat(url):
     st.markdown(f'<p style="background-color: black;color: white;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

# header("notice")

with st.sidebar:
  st.title("My Portfolio")

url01 = 'https://twilightin-titanicpred-app-titanicpred-app-48ml2g.streamlit.app/'
url02 = 'https://twilightin-topnews-app-topnews-app-nmz8mo.streamlit.app/'
url03 = 'https://twilightin-plotlyanime-app-plotlyanime-app-kpw3se.streamlit.app/'
url04 = 'https://twilightin-visionalist-covracebar-appcovracebar-app-hss31w.streamlit.app/'
url05 = 'https://twilightin-covview-app-covview-app-wf3ten.streamlit.app/'
url06 = 'https://twilightin-covdl-app-covdl-app-7xzhq6.streamlit.app/'
url07 = 'https://twilightin-app-apigpt-app-apigpt-4plb8a.streamlit.app/'


video_file01 = open('app02.mp4', 'rb')
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


#step.2 output new

# 01
st.title("入力データに応じてモデル(Xgboost)予測の結果とSHAPによるモデルの解釈")
cat('機械学習')
st.markdown("[リンク先](%s)でアプリを確認" % url01)
with st.expander("デモンストレーション(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes01)
st.markdown("""---""")

# 02
st.title("各メディアのTOPニュース(URL含め)のまとめサイト")
cat('スクレイピング')
st.markdown("[リンク先](%s)でアプリを確認" % url01)
with st.expander("デモンストレーション(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes02)
st.markdown("""---""")

# 03
st.title("各国GDPと平均寿命の相関を時系列で動的に表現")
cat('データ可視化')
annotated_text(('カテゴリ', 'データ可視化'))
st.markdown("[リンク先](%s)でアプリを確認" % url01)
with st.expander("デモンストレーション(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes03)
st.markdown("""---""")

# 04
st.title("各国のコロナ新規感染者の推移を動的に表現")
cat('データ可視化')
st.markdown("[リンク先](%s)でアプリを確認" % url01)
with st.expander("デモンストレーション(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes04)
st.markdown("""---""")

# 05
st.title("国別のコロナ新規感染者/死亡者の推移と累計")
cat('データ可視化')
st.markdown("[リンク先](%s)でアプリを確認" % url01)
with st.expander("デモンストレーション(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes05)
st.markdown("""---""")

# 06
st.title("特定国/地域のコロナ新規感染者のデータダウンロードアプリ")
cat('データ抽出')
st.markdown("[リンク先](%s)でアプリを確認" % url01)
with st.expander("デモンストレーション(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes06)
st.markdown("""---""")

# 07
st.title("ChatGPT(GPT3.5)より自分用の高度なChatGPT(text-davinci-003のAPI利用)構築")
cat('API活用')
st.markdown("[リンク先](%s)でアプリを確認" % url01)
with st.expander("デモンストレーション(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes07)
st.markdown("""---""")
