import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

# ---------------- HEADER ---------------- #
st.markdown(
    """
    <style>
      .stApp { background: #e6e9f0 !important; }
      .oss-header h1 { text-align: center; margin: 0; font-size: 28px; }
      .oss-header h4 { text-align: center; margin: 2px 0 12px 0; color: #666; font-style: italic; font-size: 14px; }
    </style>
    <div class="oss-header">
      <h1>🌍 OSS Compliance Hub</h1>
      <h4>© For EY Internal Use Only</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- CARDS LAYOUT ---------------- #
components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  :root{
    --card-bg: #ffffff;
    --card-border: #d1d5db;
    --pill-bg: #f6f7fb;
    --pill-bd: #e4e7ef;
    --btn-bg: #fff;
    --btn-border: #ccc;
  }
  body { margin:0; padding:0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }

  /* OSS awareness line */
  .oss-quote-wrap { display:flex; justify-content:center; margin: 6px 0 20px 0; }
  .oss-quote {
    width: min(900px, 85vw);
    background: #f1f1f1;
    border-left: 4px solid #7a7a7a;
    padding: 8px 12px;
    font-style: italic;
    font-size: 14px;
    border-radius: 4px;
  }

  /* Grid for 4 cards */
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px; /* space between cards */
    width: min(1000px, 90vw);
    margin: auto;
  }

  /* Individual card */
  .card {
    background: var(--card-bg);
    border: 1.5px solid var(--card-border);
    border-radius: 10px;
    padding: 14px 16px;
    transition: all 0.2s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.05);
  }
  .card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.12);
  }

  .title { margin:0 0 4px 0; font-size: 16px; }
  .tagline { margin:0 0 8px 0; color:#555; font-size: 13px; font-style: italic; }
  .pill {
    margin: 6px 0 10px 0;
    padding: 6px 8px;
    background: var(--pill-bg);
    border: 1px solid var(--pill-bd);
    border-radius: 6px;
    min-height: 32px;
    font-size: 13px;
    font-style: italic;
  }
  .open-btn {
    display: inline-block;
    padding: 6px 12px;
    font-size: 13px;
    border: 1px solid var(--btn-border);
    border-radius: 6px;
    text-decoration: none;
    color: #111;
    font-weight: 600;
    background: var(--btn-bg);
    transition: all 0.2s ease;
  }
  .open-btn:hover {
    background: #f0f0f0;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
  }
</style>
</head>
<body>

  <!-- OSS awareness -->
  <div class="oss-quote-wrap">
    <div class="oss-quote" id="oss-rotator">
      “Open Source Software (OSS) powers most of today’s technology stack.”
    </div>
  </div>

  <!-- Grid of 4 cards -->
  <div class="grid">
    <div class="card">
      <h3 class="title">Syft</h3>
      <div class="tagline"><em>Best for: SBOM generation &amp; license fetching</em></div>
      <div class="pill" id="syft-pill">🔍 Syft generates SBOMs (Software Bill of Materials).</div>
      <a class="open-btn" href="https://oss-compliance.streamlit.app/" target="_blank">Open Syft</a>
    </div>

    <div class="card">
      <h3 class="title">ScanOSS</h3>
      <div class="tagline"><em>Best for: Code snippet &amp; copyright scanning</em></div>
      <div class="pill" id="scanoss-pill">📡 ScanOSS detects open-source components from code snippets.</div>
      <a class="open-btn" href="https://oss-compliance.streamlit.app/" target="_blank">Open ScanOSS</a>
    </div>

    <div class="card">
      <h3 class="title">FOSSology</h3>
      <div class="tagline"><em>Best for: In-depth license compliance reports</em></div>
      <div class="pill" id="fossology-pill">🧩 FOSSology is an OSS license compliance toolkit.</div>
      <a class="open-btn" href="https://fosslogy.streamlit.app/" target="_blank">Open FOSSology</a>
    </div>

    <div class="card">
      <h3 class="title">ScanCode Toolkit</h3>
      <div class="tagline"><em>Best for: Licenses, copyrights &amp; SBOM export</em></div>
      <div class="pill" id="scancode-pill">📑 ScanCode detects licenses, copyrights, and dependencies.</div>
      <a class="open-btn" href="https://scancodetoolkit.streamlit.app/" target="_blank">Open ScanCode</a>
    </div>
  </div>

<script>
  const ossSlides = [
    "“Open Source Software (OSS) powers most of today’s technology stack.”",
    "“While OSS accelerates innovation, it also introduces compliance and legal risks.”",
    "“Proper OSS compliance ensures security, trust, and safe usage across projects.”"
  ];
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

  const ossEl = document.getElementById("oss-rotator");
  const syftEl = document.getElementById("syft-pill");
  const scanossEl = document.getElementById("scanoss-pill");
  const fossologyEl = document.getElementById("fossology-pill");
  const scancodeEl = document.getElementById("scancode-pill");

  let idx = 0;
  function rotate(){
    idx = (idx + 1) % ossSlides.length;
    ossEl.textContent = ossSlides[idx];
    syftEl.textContent = toolSlides.syft[idx % toolSlides.syft.length];
    scanossEl.textContent = toolSlides.scanoss[idx % toolSlides.scanoss.length];
    fossologyEl.textContent = toolSlides.fossology[idx % toolSlides.fossology.length];
    scancodeEl.textContent = toolSlides.scancode[idx % toolSlides.scancode.length];
  }
  setInterval(rotate, 5000);
</script>

</body>
</html>
    """,
    height=650,
    scrolling=False,
)
