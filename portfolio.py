import pandas as pd
import streamlit as st
from annotated_text import annotated_text

def header(url):
     st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{url}</p>', unsafe_allow_html=True)

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

video_file3 = open('app03.mp4', 'rb')
video_bytes3 = video_file3.read()

video_file4 = open('app04.mp4', 'rb')
video_bytes4 = video_file4.read()

video_file5 = open('app05.mp4', 'rb')
video_bytes5 = video_file5.read()

video_file6 = open('app06.mp4', 'rb')
video_bytes6 = video_file6.read()

video_file7 = open('app07.mp4', 'rb')
video_bytes7 = video_file7.read()

#step.2 output new

# 01
st.title("���̓f�[�^�ɉ����ă��f��(Xgboost)�\���̌��ʂ�SHAP�ɂ�郂�f���̉���")
annotated_text(('�J�e�S��', '�@�B�w�K'))
st.markdown("[�����N��](%s)�ŃA�v�����m�F" % url01)
with st.expander("�f�����X�g���[�V����(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes01)
st.markdown("""---""")

# 02
st.title("�e���f�B�A��TOP�j���[�X(URL�܂�)�̂܂Ƃ߃T�C�g")
annotated_text(('�J�e�S��', '�X�N���C�s���O'))
st.markdown("[�����N��](%s)�ŃA�v�����m�F" % url01)
with st.expander("�f�����X�g���[�V����(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes02)
st.markdown("""---""")

# 03
st.title("�e��GDP�ƕ��ώ����̑��ւ����n��œ��I�ɕ\��")
annotated_text(('�J�e�S��', '�f�[�^����'))
st.markdown("[�����N��](%s)�ŃA�v�����m�F" % url01)
with st.expander("�f�����X�g���[�V����(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes03)
st.markdown("""---""")

# 04
st.title("�e���̃R���i�V�K�����҂̐��ڂ𓮓I�ɕ\��")
annotated_text(('�J�e�S��', '�f�[�^����'))
st.markdown("[�����N��](%s)�ŃA�v�����m�F" % url01)
with st.expander("�f�����X�g���[�V����(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes04)
st.markdown("""---""")

# 05
st.title("���ʂ̃R���i�V�K������/���S�҂̐��ڂƗ݌v")
annotated_text(('�J�e�S��', '�f�[�^����'))
st.markdown("[�����N��](%s)�ŃA�v�����m�F" % url01)
with st.expander("�f�����X�g���[�V����(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes05)
st.markdown("""---""")

# 06
st.title("���荑/�n��̃R���i�V�K�����҂̃f�[�^�_�E�����[�h�A�v��")
annotated_text(('�J�e�S��', '�f�[�^���o'))
st.markdown("[�����N��](%s)�ŃA�v�����m�F" % url01)
with st.expander("�f�����X�g���[�V����(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes06)
st.markdown("""---""")

# 07
st.title("ChatGPT(GPT3.5)��莩���p�̍��x��ChatGPT(text-davinci-003��API���p)�\�z")
annotated_text(('�J�e�S��', 'API'))
st.markdown("[�����N��](%s)�ŃA�v�����m�F" % url01)
with st.expander("�f�����X�g���[�V����(10s)"):
    st.write('A simple video demo created by myself.')
    st.video(video_bytes07)
st.markdown("""---""")
