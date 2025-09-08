import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

# Page background + header
st.markdown(
    """
    <style>
      .stApp { background: #e6e9f0 !important; } /* solid background outside the rectangle */
      .oss-header h1, .oss-header h4 { text-align: center; margin: 0.25rem 0; }
      .oss-header h4 { color: #666; font-style: italic; font-weight: 500; }
    </style>
    <div class="oss-header">
      <h1>🌍 OSS Compliance Hub</h1>
      <h4>© For EY Internal Use Only</h4>
    </div>
    """,
    unsafe_allow_html=True
)

# Self-contained HTML/CSS/JS (no while-loops) for:
# 1) Highlighted OSS slides (separate, above rectangle)
# 2) Centered rectangle split into 4 boxes with rotating lines in each
components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  :root{
    --outer-bg: transparent;     /* Streamlit handles page bg */
    --box-bg: #ffffff;           /* rectangle background */
    --border: #2f3136;           /* outer border color */
    --inner: #2f3136;            /* inner lines for the plus */
    --muted: #555;               /* tagline color */
    --pill-bg: #f6f7fb;          /* slide pill bg */
    --pill-bd: #e4e7ef;          /* slide pill border */
    --hi-bg: #f1f1f1;            /* OSS line highlight bg */
    --hi-bd: #7a7a7a;            /* OSS line left border */
  }
  html, body {
    margin: 0; padding: 0; background: var(--outer-bg);
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }

  /* OSS awareness lines (separate, above rectangle) */
  .oss-quote-wrap {
    display:flex; justify-content:center; width:100%;
    margin: 14px 0 22px 0;
  }
  .oss-quote {
    width: min(1000px, 85vw);
    background: var(--hi-bg);
    border-left: 5px solid var(--hi-bd);
    padding: 12px 16px;
    font-style: italic;
    font-size: 15.5px;
    border-radius: 6px;
  }

  /* Centered rectangle wrapper */
  .pane-wrap{
    display:flex; justify-content:center; width:100%;
    padding: 6px 0 40px;
  }

  /* Outer rectangle (window) */
  .pane{
    width: min(1100px, 92vw);
    background: var(--box-bg);
    border: 4px solid var(--border);
    border-radius: 14px;
    overflow: hidden;
    box-shadow: 0 6px 22px rgba(0,0,0,0.08);
  }

  /* 2x2 grid using table → crisp single inner “+” lines */
  table.grid{
    width: 100%;
    border-collapse: collapse; /* makes inner borders merge → plus shape */
    table-layout: fixed;       /* equal cell widths */
  }
  table.grid td{
    border: 2px solid var(--inner);
    padding: 18px 16px;
    vertical-align: top;
    height: 240px; /* tweak if you want taller cells */
  }

  /* Cell content */
  .title { margin: 0 0 6px 0; font-size: 20px; }
  .tagline { margin: 0 0 12px 0; color: var(--muted); font-size: 14.5px; font-style: italic; }
  .pill {
    margin: 10px 0 14px 0;
    padding: 10px 12px;
    background: var(--pill-bg);
    border: 1px solid var(--pill-bd);
    border-radius: 8px;
    min-height: 44px;
    display: flex; align-items: center;
    font-size: 14.5px;
    font-style: italic; /* all text lines italic as requested */
  }
  .open-btn {
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
  .open-btn:hover { box-shadow: 0 4px 14px rgba(0,0,0,0.08); }
  .open-btn:active { transform: translateY(1px); }
</style>
</head>
<body>

  <!-- OSS awareness (quoted + highlighted) -->
  <div class="oss-quote-wrap">
    <div class="oss-quote" id="oss-rotator">
      "Open Source Software (OSS) powers most of today’s technology stack."
    </div>
  </div>

  <!-- Centered rectangle divided into 4 equal boxes (plus-shaped inner lines) -->
  <div class="pane-wrap">
    <div class="pane">
      <table class="grid">
        <tr>
          <td>
            <h3 class="title">Syft</h3>
            <div class="tagline"><em>Best for: SBOM generation &amp; license fetching</em></div>
            <div class="pill" id="syft-pill">🔍 Syft generates SBOMs (Software Bill of Materials).</div>
            <a class="open-btn" href="https://oss-compliance.streamlit.app/" target="_blank" rel="noopener">Open Syft</a>
          </td>
          <td>
            <h3 class="title">ScanOSS</h3>
            <div class="tagline"><em>Best for: Code snippet &amp; copyright scanning</em></div>
            <div class="pill" id="scanoss-pill">📡 ScanOSS detects open-source components from code snippets.</div>
            <a class="open-btn" href="https://oss-compliance.streamlit.app/" target="_blank" rel="noopener">Open ScanOSS</a>
          </td>
        </tr>
        <tr>
          <td>
            <h3 class="title">FOSSology</h3>
            <div class="tagline"><em>Best for: In-depth license compliance reports</em></div>
            <div class="pill" id="fossology-pill">🧩 FOSSology is an OSS license compliance toolkit.</div>
            <a class="open-btn" href="https://fosslogy.streamlit.app/" target="_blank" rel="noopener">Open FOSSology</a>
          </td>
          <td>
            <h3 class="title">ScanCode Toolkit</h3>
            <div class="tagline"><em>Best for: Licenses, copyrights &amp; SBOM export</em></div>
            <div class="pill" id="scancode-pill">📑 ScanCode detects licenses, copyrights, and dependencies.</div>
            <a class="open-btn" href="https://scancodetoolkit.streamlit.app/" target="_blank" rel="noopener">Open ScanCode</a>
          </td>
        </tr>
      </table>
    </div>
  </div>

<script>
  // OSS awareness rotating quotes
  const ossSlides = [
    "“Open Source Software (OSS) powers most of today’s technology stack.”",
    "“While OSS accelerates innovation, it also introduces compliance and legal risks.”",
    "“Proper OSS compliance ensures security, trust, and safe usage across projects.”"
  ];

  // Tool-specific rotating lines
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

  // Start auto-rotation every 5s
  setInterval(rotate, 5000);
</script>

</body>
</html>
    """,
    height=820,
    scrolling=False,
)
