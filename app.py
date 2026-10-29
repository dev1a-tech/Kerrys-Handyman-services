"""
app.py — Streamlit version of the Kerry's Handyman Service LLC website.

Run on your computer:
    pip3 install -r requirements.txt
    streamlit run app.py

Deploy free on Streamlit Community Cloud:
    share.streamlit.io → Create app → pick this GitHub repo → Main file: app.py

The page content comes from build_site.py, so edit the CONFIG block there
and both the Streamlit app and index.html stay in sync.
"""

import sys
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

# Make sure build_site.py (in the same folder) can be imported anywhere
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_site import CONFIG, build  # noqa: E402

st.set_page_config(
    page_title=f"{CONFIG['name']} {CONFIG['tagline']} | {CONFIG['town']}",
    page_icon="🔧",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit's own menu, header, footer and padding so only the site shows,
# and make the website fill the whole browser window.
st.markdown(
    """
    <style>
      #MainMenu, header, footer, [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"] {display: none !important;}
      .block-container, [data-testid="stMainBlockContainer"] {
          padding: 0 !important; max-width: 100% !important;
      }
      [data-testid="stAppViewContainer"], .main {padding: 0 !important;}
      [data-testid="stVerticalBlock"] {gap: 0 !important;}
      [data-testid="stElementContainer"]:has(style) {display: none !important;}
      iframe {height: 100vh !important; width: 100% !important; border: 0; display: block;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Phone links need to open outside the embedded frame to work on phones.
html = build().replace('href="tel:', 'target="_top" href="tel:')

components.html(html, height=900, scrolling=True)
