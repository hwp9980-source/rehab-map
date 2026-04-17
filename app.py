import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(
    page_title="제3기 회복기재활의료기관 접근성 지도",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS로 패딩·여백 제거
st.markdown("""
<style>
  [data-testid="stAppViewContainer"] { padding: 0; }
  [data-testid="stHeader"] { display: none; }
  [data-testid="stToolbar"] { display: none; }
  .block-container { padding: 0 !important; max-width: 100% !important; }
  iframe { display: block; }
</style>
""", unsafe_allow_html=True)

html_content = Path("Rehab_Map_v3.html").read_text(encoding="utf-8")
components.html(html_content, height=900, scrolling=False)
