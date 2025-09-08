import streamlit as st
import itertools
import time

# ---------------- CONFIG ---------------- #
OSS_SLIDES = itertools.cycle([
    '"Open Source Software (OSS) powers most of today’s technology stack."',
    '"While OSS accelerates innovation, it also introduces compliance and legal risks."',
    '"Proper OSS compliance ensures security, trust, and safe usage across projects."'
])

TOOL_SLIDES = {
    "Syft": {
        "slides": itertools.cycle([
            "*🔍 Syft generates SBOMs (Software Bill of Materials).*",
            "*Helps track dependencies and their licenses.*",
            "*Useful for compliance, vulnerability scanning, and audits.*"
        ]),
        "tagline": "*Best for: SBOM generation & license fetching*",
        "link": "https://oss-compliance.streamlit.app/"
    },
    "ScanOSS": {
        "slides": itertools.cycle([
            "*📡 ScanOSS detects open-source components from code snippets.*",
            "*Matches code against a global OSS knowledge base.*",
            "*Great for identifying license and copyright risks.*"
        ]),
        "tagline": "*Best for: Code snippet & copyright scanning*",
        "link": "https://oss-compliance.streamlit.app/"
    },
    "Fossology": {
        "slides": itertools.cycle([
            "*🧩 Fossology is an OSS license compliance toolkit.*",
            "*Provides multiple scanning agents (nomos, monk, ojo, etc.).*",
            "*Generates detailed reports for enterprise governance.*"
        ]),
        "tagline": "*Best for: In-depth license compliance reports*",
        "link": "https://fosslogy.streamlit.app/"
    },
    "ScanCode Toolkit": {
        "slides": itertools.cycle([
            "*📑 ScanCode detects licenses, copyrights, and dependencies.*",
            "*Supports SBOM export in SPDX & CycloneDX formats.*",
            "*Widely used for in-depth OSS compliance analysis.*"
        ]),
        "tagline": "*Best for: Licenses, copyrights & SBOM export*",
        "link": "https://scancodetoolkit.streamlit.app/"
    }
}

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

# ---------------- HEADER ---------------- #
st.markdown(
    """
    <h1 style='text-align:center;'>🌍 OSS Compliance Hub</h1>
    <h4 style='text-align:center; color:gray;'>© For EY Internal Use Only</h4>
    """,
    unsafe_allow_html=True
)

# ---------------- OSS SLIDES ---------------- #
oss_placeholder = st.empty()

# ---------------- SCANNER RECTANGLE ---------------- #
st.markdown(
    """
    <style>
        .scanner-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            grid-template-rows: 1fr 1fr;
            width: 70%;
            margin: auto;
            border: 3px solid #444;
            border-radius: 12px;
            overflow: hidden;
            background-color: #ffffff;
        }
        .scanner-cell {
            border: 1px solid #444;
            padding: 18px;
            text-align: center;
        }
        .slide-box {
            margin: 10px auto;
            padding: 10px;
            background: #f7f7f7;
            border: 1px solid #ddd;
            border-radius: 8px;
            font-style: italic;
        }
        .oss-box {
            text-align: center;
            margin: 20px auto;
            padding: 12px;
            background: #f0f0f0;
            border-left: 4px solid #666;
            width: 70%;
            font-style: italic;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='scanner-grid'>", unsafe_allow_html=True)

tool_placeholders = {}
for tool, config in TOOL_SLIDES.items():
    st.markdown("<div class='scanner-cell'>", unsafe_allow_html=True)
    st.subheader(tool)
    st.caption(config["tagline"])
    tool_placeholders[tool] = st.empty()
    if st.button(f"Open {tool}", key=tool):
        st.markdown(f"[Click here if not redirected]({config['link']})")
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LIVE SLIDES ---------------- #
while True:
    oss_placeholder.markdown(f"<div class='oss-box'>{next(OSS_SLIDES)}</div>", unsafe_allow_html=True)
    for tool, config in TOOL_SLIDES.items():
        tool_placeholders[tool].markdown(
            f"<div class='slide-box'>{next(config['slides'])}</div>", unsafe_allow_html=True
        )
    time.sleep(5)
