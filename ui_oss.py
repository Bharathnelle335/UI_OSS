import streamlit as st
import itertools
import time
import webbrowser

# ---------------- CONFIG ---------------- #
OSS_SLIDES = itertools.cycle([
    "Open Source Software (OSS) powers most of today’s technology stack.",
    "While OSS accelerates innovation, it also introduces compliance and legal risks.",
    "Proper OSS compliance ensures security, trust, and safe usage across projects."
])

TOOL_SLIDES = {
    "Syft": {
        "slides": itertools.cycle([
            "🔍 Syft generates SBOMs (Software Bill of Materials).",
            "Helps track dependencies and their licenses.",
            "Useful for compliance, vulnerability scanning, and audits."
        ]),
        "tagline": "Best for: **SBOM generation & license fetching**",
        "link": "https://oss-compliance.streamlit.app/"
    },
    "ScanOSS": {
        "slides": itertools.cycle([
            "📡 ScanOSS detects open-source components from code snippets.",
            "Matches code against a global OSS knowledge base.",
            "Great for identifying license and copyright risks."
        ]),
        "tagline": "Best for: **Code snippet & copyright scanning**",
        "link": "https://oss-compliance.streamlit.app/"
    },
    "Fossology": {
        "slides": itertools.cycle([
            "🧩 Fossology is an OSS license compliance toolkit.",
            "Provides multiple scanning agents (nomos, monk, ojo, etc.).",
            "Generates detailed reports for enterprise governance."
        ]),
        "tagline": "Best for: **In-depth license compliance reports**",
        "link": "https://fosslogy.streamlit.app/"
    },
    "ScanCode Toolkit": {
        "slides": itertools.cycle([
            "📑 ScanCode detects licenses, copyrights, and dependencies.",
            "Supports SBOM export in SPDX & CycloneDX formats.",
            "Widely used for in-depth OSS compliance analysis."
        ]),
        "tagline": "Best for: **Licenses, copyrights & SBOM export**",
        "link": "https://scancodetoolkit.streamlit.app/"
    }
}

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

# CSS Styling
st.markdown(
    """
    <style>
        body {
            background-color: #e6e9f0; /* solid background */
        }
        .scanner-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            gap: 0px;
            border: 4px solid #333333;
            border-radius: 12px;
            background-color: #ffffff; /* rectangle box */
            overflow: hidden;
            margin: auto;
            width: 80%;
        }
        .scanner-cell {
            border: 2px solid #333333;
            padding: 20px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ---------------- #
st.markdown(
    """
    <h1 style='text-align:center;'>🌍 OSS Compliance Hub</h1>
    <h4 style='text-align:center; color:gray;'>© For EY Internal Use Only</h4>
    """,
    unsafe_allow_html=True
)

oss_placeholder = st.empty()

# ---------------- SCANNER GRID ---------------- #
st.markdown("<div class='scanner-grid'>", unsafe_allow_html=True)

tool_names = list(TOOL_SLIDES.keys())
tool_placeholders = {}

for tool in tool_names:
    st.markdown("<div class='scanner-cell'>", unsafe_allow_html=True)
    st.subheader(tool)
    st.caption(TOOL_SLIDES[tool]["tagline"])
    tool_placeholders[tool] = st.empty()
    if st.button(f"➡ Open {tool} UI", key=tool):
        st.markdown(f"[Click here if not redirected]({TOOL_SLIDES[tool]['link']})")
        webbrowser.open_new_tab(TOOL_SLIDES[tool]["link"])
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LIVE SLIDES ---------------- #
while True:
    oss_placeholder.info(next(OSS_SLIDES))
    for tool, config in TOOL_SLIDES.items():
        tool_placeholders[tool].success(next(config["slides"]))
    time.sleep(5)
