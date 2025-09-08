import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  /* Full-page background (lighter effect) */
  body {
    margin: 0;
    padding: 0;
    height: 100vh;
    background: url("https://raw.githubusercontent.com/Bharathnelle335/UI_OSS/main/image.jpg") no-repeat center center fixed;
    background-size: cover;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }
  body::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(255,255,255,0.2); /* light overlay to soften the blue bg */
    z-index: -1;
  }

  /* Header */
  .oss-header h1 {
    text-align: center;
    margin: 0;
    font-size: 28px;
    color: #ffffff; /* bright white */
    text-shadow: 0 2px 4px rgba(0,0,0,0.4);
  }
  .oss-header h4 {
    text-align: center;
    margin: 2px 0 10px 0;
    color: #f5f5f5; /* lighter gray */
    font-style: italic;
    font-size: 14px;
  }

  /* OSS awareness line */
  .oss-quote-wrap { display:flex; justify-content:center; margin: 6px 0 16px 0; }
  .oss-quote {
    width: min(900px, 85vw);
    background: rgba(0,0,0,0.5);
    border-left: 4px solid #fff;
    padding: 6px 10px;
    font-style: italic;
    font-size: 14px;
    border-radius: 4px;
    color: #fff;
  }

  /* Grid for 4 cards */
  .grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    width: min(1000px, 90vw);
    margin: auto;
  }

  /* Individual card (semi-transparent) */
  .card {
    background: rgba(255,255,255,0.8); /* transparent white */
    border: 1.5px solid rgba(209,213,219,0.6);
    border-radius: 10px;
    padding: 12px 14px;
    transition: all 0.2s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  }
  .card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.3);
    background: rgba(255,255,255,0.9); /* brighten a bit on hover */
  }

  .title { margin:0 0 4px 0; font-size: 16px; color:#111; }
  .tagline { margin:0 0 8px 0; color:#333; font-size: 13px; font-style: italic; }
  .pill {
    margin: 6px 0 10px 0;
    padding: 6px 8px;
    background: rgba(246,247,251,0.9);
    border: 1px solid #e4e7ef;
    border-radius: 6px;
    min-height: 32px;
    font-size: 13px;
    font-style: italic;
  }
  .open-btn {
    display: inline-block;
    padding: 6px 12px;
    font-size: 13px;
    border: 1px solid #bbb;
    border-radius: 6px;
    text-decoration: none;
    color: #111;
    font-weight: 600;
    background: rgba(255,255,255,0.85);
    transition: all 0.2s ease;
  }
  .open-btn:hover {
    background: #f0f0f0;
    box-shadow: 0 3px 10px rgba(0,0,0,0.2);
  }
</style>
</head>
<body>

  <div class="oss-header">
    <h1>OSS Compliance Hub</h1>
    <h4>© For EY Internal Use Only</h4>
  </div>

  <div class="oss-quote-wrap">
    <div class="oss-quote" id="oss-rotator">
      “Open Source Software (OSS) powers most of today’s technology stack.”
    </div>
  </div>

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
    height=720,
    scrolling=False,
)
