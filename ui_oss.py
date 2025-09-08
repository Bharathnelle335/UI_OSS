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

# ---------------- UI CONFIG ---------------- #
st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

# Page background color
st.markdown(
    """
    <style>
        body {
            background-color: #f0f2f6; /* solid background */
        }
        .scanner-box {
            border: 3px solid #cccccc;
            border-radius: 15px;
            padding: 25px;
            background-color: #ffffff; /* light rectangle */
            position: relative;
        }
        .plus-symbol {
            position: absolute;
            top: 50%;
            left: 50%;
            font-size: 40px;
            font-weight: bold;
            color: #666666;
            transform: translate(-50%, -50%);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- HEADER ---------------- #
st.markdown(
    "<h1 style='text-align:center;'>🌍 OSS Compliance Hub <span style='font-size:16px; color:gray;'>(For EY Internal Use Only)</span></h1>",
    unsafe_allow_html=True
)

oss_placeholder = st.empty()

# ---------------- SCANNER RECTANGLE ---------------- #
st.markdown("<div class='scanner-box'>", unsafe_allow_html=True)

cols = st.columns(2)
tool_placeholders = {}

tool_names = list(TOOL_SLIDES.keys())
for i, col in enumerate(cols):
    with col:
        for j in range(2):  # 2 rows = 4 tools total
            tool = tool_names[i*2 + j]
            st.subheader(tool)
            st.caption(TOOL_SLIDES[tool]["tagline"])
            tool_placeholders[tool] = st.empty()

            if st.button(f"➡ Open {tool} UI", key=tool):
                st.write(f"Opening {tool} UI...")
                st.markdown(f"[Click here if not redirected]({TOOL_SLIDES[tool]['link']})")
                webbrowser.open_new_tab(TOOL_SLIDES[tool]["link"])

# Add plus symbol in the center of the rectangle
st.markdown("<div class='plus-symbol'>+</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---------------- LIVE SLIDES ---------------- #
while True:
    oss_placeholder.info(next(OSS_SLIDES))
    for tool, config in TOOL_SLIDES.items():
        tool_placeholders[tool].success(next(config["slides"]))
    time.sleep(5)
