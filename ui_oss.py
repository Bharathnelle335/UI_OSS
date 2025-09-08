import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

st.markdown(
    """
    <style>
      .stApp { background: #e6e9f0 !important; }
      .oss-header h1 { text-align: center; margin: 0; font-size: 28px; }
      .oss-header h4 { text-align: center; margin: 2px 0 8px 0; color: #666; font-style: italic; font-size: 14px; }
    </style>
    <div class="oss-header">
      <h1>🌍 OSS Compliance Hub</h1>
      <h4>© For EY Internal Use Only</h4>
    </div>
    """,
    unsafe_allow_html=True
)

components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  :root{
    --border: #2f3136;
    --pill-bg: #f6f7fb;
    --pill-bd: #e4e7ef;
    --hi-bg: #f1f1f1;
    --hi-bd: #7a7a7a;
  }
  body { margin:0; padding:0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; }

  /* OSS awareness line */
  .oss-quote-wrap { display:flex; justify-content:center; margin: 6px 0 14px 0; }
  .oss-quote {
    width: min(900px, 85vw);
    background: var(--hi-bg);
    border-left: 4px solid var(--hi-bd);
    padding: 8px 12px;
    font-style: italic;
    font-size: 14px;
    border-radius: 4px;
  }

  /* Rectangle */
  .pane-wrap { display:flex; justify-content:center; }
  .pane {
    width: min(1000px, 90vw);
    background: #fff;
    border: 3px solid var(--border);
    border-radius: 10px;
    overflow: hidden;
  }

  table.grid { width:100%; border-collapse: collapse; table-layout: fixed; }
  table.grid td {
    border: 1.5px solid var(--border);
    padding: 12px 10px;
    vertical-align: top;
    height: 170px; /* compact height */
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
    padding: 6px 10px;
    font-size: 13px;
    border: 1px solid #ccc;
    border-radius: 6px;
    text-decoration: none;
    color: #111;
    font-weight: 600;
    background: #fff;
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

  <!-- Rectangle with 4 boxes -->
  <div class="pane-wrap">
    <div class="pane">
      <table class="grid">
        <tr>
          <td>
            <h3 class="title">Syft</h3>
            <div class="tagline"><em>Best for: SBOM generation & license fetching</em></div>
            <div class="pill" id="syft-pill">🔍 Syft generates SBOMs (Software Bill of Materials).</div>
            <a class="open-btn" href="https://oss-compliance.streamlit.app/" target="_blank">Open Syft</a>
          </td>
          <td>
            <h3 class="title">ScanOSS</h3>
            <div class="tagline"><em>Best for: Code snippet & copyright scanning</em></div>
            <div class="pill" id="scanoss-pill">📡 ScanOSS detects open-source components from code snippets.</div>
            <a class="open-btn" href="https://oss-compliance.streamlit.app/" target="_blank">Open ScanOSS</a>
          </td>
        </tr>
        <tr>
          <td>
            <h3 class="title">FOSSology</h3>
            <div class="tagline"><em>Best for: In-depth license compliance reports</em></div>
            <div class="pill" id="fossology-pill">🧩 FOSSology is an OSS license compliance toolkit.</div>
            <a class="open-btn" href="https://fosslogy.streamlit.app/" target="_blank">Open FOSSology</a>
          </td>
          <td>
            <h3 class="title">ScanCode Toolkit</h3>
            <div class="tagline"><em>Best for: Licenses, copyrights & SBOM export</em></div>
            <div class="pill" id="scancode-pill">📑 ScanCode detects licenses, copyrights, and dependencies.</div>
            <a class="open-btn" href="https://scancodetoolkit.streamlit.app/" target="_blank">Open ScanCode</a>
          </td>
        </tr>
      </table>
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
    height=640,  # reduced so everything fits
    scrolling=False,
)
