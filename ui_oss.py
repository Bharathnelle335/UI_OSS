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

# ---------------- UI ---------------- #
st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

# Top OSS Section
st.markdown("<h1 style='text-align:center;'>🌍 OSS Compliance Hub</h1>", unsafe_allow_html=True)
oss_placeholder = st.empty()

# Tool Grid Section
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
            
            # Use button instead of link
            if st.button(f"➡ Open {tool} UI", key=tool):
                st.write(f"Opening {tool} UI...")
                st.markdown(f"[Click here if not redirected]({TOOL_SLIDES[tool]['link']})")
                webbrowser.open_new_tab(TOOL_SLIDES[tool]["link"])

# ---------------- Live Updating Slides ---------------- #
while True:
    # Update OSS top section
    oss_placeholder.info(next(OSS_SLIDES))

    # Update each tool section
    for tool, config in TOOL_SLIDES.items():
        tool_placeholders[tool].success(next(config["slides"]))

    time.sleep(5)  # refresh every 5s
