import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

# Page header + solid background (kept simple & robust)
st.markdown(
    """
    <style>
      /* Solid background for the whole UI */
      .stApp { background: #e6e9f0 !important; }
      /* Center the header text cleanly */
      .oss-header h1, .oss-header h4 { text-align: center; margin: 0.2rem 0; }
      .oss-header h4 { color: #666; font-weight: 500; }
    </style>
    <div class="oss-header">
      <h1>🌍 OSS Compliance Hub</h1>
      <h4>© For EY Internal Use Only</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# Self-contained HTML/CSS/JS for the window box and rotating slides
components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  :root{
    --bg: #e6e9f0;
    --box-bg: #ffffff;
    --border: #2f3136;
    --inner: #2f3136;
  }
  html, body{
    margin:0; padding:0; background: transparent; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }

  /* Wrapper to center the window box */
  .wrap{
    display:flex; justify-content:center; align-items:flex-start;
    width:100%;
    padding: 12px 0 40px;
    background: transparent; /* page background is handled by Streamlit */
  }

  /* Outer rectangle (window) */
  .window{
    width: min(1100px, 92vw);
    background: var(--box-bg);
    border: 4px solid var(--border);
    border-radius: 14px;
    overflow: hidden; /* keeps rounded corners for inner content */
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
  }

  /* Top moving info line */
  .top-info{
    padding: 12px 18px;
    background: #f7f8fb;
    border-bottom: 1px solid #e5e7eb;
    font-size: 14.5px;
  }

  /* 2x2 grid using a table so borders collapse cleanly into a “+” */
  .grid{
    width: 100%;
    border-collapse: collapse; /* ensures single inner lines (plus shape) */
    table-layout: fixed;       /* equal cells */
  }
  .grid td{
    border: 2px solid var(--inner); /* inner lines that form the plus */
    padding: 16px 18px;
    vertical-align: top;
    height: 240px; /* adjust as you like */
  }

  /* Cell content styling */
  .tool-title{
    margin: 0 0 6px 0;
    font-size: 20px;
  }
  .tagline{
    margin: 0 0 12px 0;
    color: #555;
    font-size: 14px;
  }
  .slide{
    margin: 10px 0 16px 0;
    padding: 10px 12px;
    background: #f5f7fb;
    border: 1px solid #e6e8ef;
    border-radius: 8px;
    min-height: 56px;
    display: flex; align-items: center;
    font-size: 14.5px;
  }
  .btn{
    display: inline-block;
    padding: 10px 14px;
    border: 1px solid #d0d4dc;
    border-radius: 10px;
    text-decoration: none;
    color: #111;
    font-weight: 600;
    background: #fff;
    transition: box-shadow .15s ease, transform .04s ease;
  }
  .btn:hover{ box-shadow: 0 4px 14px rgba(0,0,0,0.08); }
  .btn:active{ transform: translateY(1px); }
</style>
</head>
<body>

<div class="wrap">
  <div class="window">

    <!-- Rotating top info line -->
    <div class="top-info" id="oss-rotator">Open Source Software (OSS) powers most of today’s technology stack.</div>

    <!-- 2x2 window pane (outer rectangle + inner “+” lines) -->
    <table class="grid">
      <tr>
        <td>
          <h3 class="tool-title">Syft</h3>
          <div class="tagline">Best for: <b>SBOM generation & license fetching</b></div>
          <div class="slide" id="syft-slide">🔍 Syft generates SBOMs (Software Bill of Materials).</div>
          <a class="btn" href="https://oss-compliance.streamlit.app/" target="_blank" rel="noopener">Open Syft UI</a>
        </td>
        <td>
          <h3 class="tool-title">ScanOSS</h3>
          <div class="tagline">Best for: <b>Code snippet & copyright scanning</b></div>
          <div class="slide" id="scanoss-slide">📡 ScanOSS detects open-source components from code snippets.</div>
          <a class="btn" href="https://oss-compliance.streamlit.app/" target="_blank" rel="noopener">Open ScanOSS UI</a>
        </td>
      </tr>
      <tr>
        <td>
          <h3 class="tool-title">FOSSology</h3>
          <div class="tagline">Best for: <b>In-depth license compliance reports</b></div>
          <div class="slide" id="fossology-slide">🧩 FOSSology is an OSS license compliance toolkit.</div>
          <a class="btn" href="https://fosslogy.streamlit.app/" target="_blank" rel="noopener">Open FOSSology UI</a>
        </td>
        <td>
          <h3 class="tool-title">ScanCode Toolkit</h3>
          <div class="tagline">Best for: <b>Licenses, copyrights & SBOM export</b></div>
          <div class="slide" id="scancode-slide">📑 ScanCode detects licenses, copyrights, and dependencies.</div>
          <a class="btn" href="https://scancodetoolkit.streamlit.app/" target="_blank" rel="noopener">Open ScanCode UI</a>
        </td>
      </tr>
    </table>

  </div>
</div>

<script>
  // Top rotating OSS lines
  const ossSlides = [
    "Open Source Software (OSS) powers most of today’s technology stack.",
    "While OSS accelerates innovation, it also introduces compliance and legal risks.",
    "Proper OSS compliance ensures security, trust, and safe usage across projects."
  ];

  // Tool-specific rotating slides
  const toolSlides = {
    syft: [
      "🔍 Syft generates SBOMs (Software Bill of Materials).",
      "Helps track dependencies and their licenses.",
      "Useful for compliance, vulnerability scanning, and audits."
    ],
    scanoss: [
      "📡 ScanOSS detects open-source components from code snippets.",
      "Matches code against a global OSS knowledge base.",
      "Great for identifying license and copyright risks."
    ],
    fossology: [
      "🧩 FOSSology is an OSS license compliance toolkit.",
      "Provides multiple scanning agents (nomos, monk, ojo, etc.).",
      "Generates detailed reports for enterprise governance."
    ],
    scancode: [
      "📑 ScanCode detects licenses, copyrights, and dependencies.",
      "Supports SBOM export in SPDX & CycloneDX formats.",
      "Widely used for in-depth OSS compliance analysis."
    ]
  };

  // Elements
  const ossEl = document.getElementById("oss-rotator");
  const syftEl = document.getElementById("syft-slide");
  const scanossEl = document.getElementById("scanoss-slide");
  const fossologyEl = document.getElementById("fossology-slide");
  const scancodeEl = document.getElementById("scancode-slide");

  let idx = 0;
  function rotate(){
    idx = (idx + 1) % ossSlides.length;
    ossEl.textContent = ossSlides[idx];

    syftEl.textContent = toolSlides.syft[idx % toolSlides.syft.length];
    scanossEl.textContent = toolSlides.scanoss[idx % toolSlides.scanoss.length];
    fossologyEl.textContent = toolSlides.fossology[idx % toolSlides.fossology.length];
    scancodeEl.textContent = toolSlides.scancode[idx % toolSlides.scancode.length];
  }

  // Initial + 5s interval
  setInterval(rotate, 5000);
</script>

</body>
</html>
    """,
    height=720,
    scrolling=False,
)
