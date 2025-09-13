import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="OSS Compliance Dashboard", layout="wide")

# ---------------- Sidebar: Ani (help bot) ----------------
with st.sidebar:
    st.header("🤖 Ani")
    st.caption("Quick help & FAQ for this dashboard")

    queries = [
        "How is this UI useful for OSS compliance?",
        "What does ScanOSS do?",
        "What does ScanCode Toolkit do?",
        "What does FOSSology do?",
        "What does Syft do?",
        "Where do these links go?",
        "Do I need any special access or token?",
        "Does this upload my source code?",
    ]
    q = st.radio("Queries", queries, index=0)

    answers = {
        "How is this UI useful for OSS compliance?": (
            "- Centralizes entry points to the main OSS compliance tools used internally.\n"
            "- Lets teams quickly choose the right tool for **license discovery**, **SBOM**, and **copyright** checks.\n"
            "- Keeps a consistent, EY-branded landing experience."
        ),
        "What does ScanOSS do?": (
            "- Detects open-source components from code (including snippets) against a global knowledge base.\n"
            "- Useful for early identification of **license** and **copyright** risks."
        ),
        "What does ScanCode Toolkit do?": (
            "- Deep **license detection**, **copyright** discovery.\n"
            "- Can export **SBOM** in **SPDX** / **CycloneDX** formats."
        ),
        "What does FOSSology do?": (
            "- Enterprise-grade license compliance toolkit with multiple agents (nomos, monk, ojo, etc.).\n"
            "- Generates detailed reports for governance and audits."
        ),
        "What does Syft do?": (
            "- Generates **SBOMs** from images or file systems.\n"
            "- Helpful to inventory dependencies and collect license fields for compliance workflows."
        ),
        "Where do these links go?": (
            "- Each card opens a dedicated Streamlit app for that tool:\n"
            "  - **ScanOSS** → internal ScanOSS scanning UI\n"
            "  - **ScanCode Toolkit** → in-depth license/SBOM UI\n"
            "  - **FOSSology** → compliance reporting UI\n"
            "  - **Syft** → SBOM generation UI"
        ),
        "Do I need any special access or token?": (
            "- Generally you can browse public repos without tokens.\n"
            "- For private resources or higher API limits, use a GitHub token in the relevant app."
        ),
        "Does this upload my source code?": (
            "- Depends on the specific tool/app and configuration.\n"
            "- Many workflows scan locally or within your controlled CI environment.\n"
            "- Always follow internal data-handling policies."
        ),
    }

    st.markdown("---")
    st.markdown(f"**Answer:**\n\n{answers.get(q, 'Select a question to view the answer.')}")

# ---------------- Main HTML dashboard (as provided) ----------------
components.html(
    """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<style>
  /* Full-page background */
  body {
    margin: 0;
    padding: 0;
    height: 100vh;
    background: url("https://raw.githubusercontent.com/Bharathnelle335/UI_OSS/main/white.jpg") no-repeat center center fixed;
    background-size: cover;
    font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif;
  }
  body::before {
    content: "";
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background: rgba(255,255,255,0.2);
    z-index: -1;
  }

  /* Header container with gradient background */
  .oss-header {
    background: linear-gradient(90deg, #0f2027, #2c5364, #0f2027);
    padding: 12px 0;
    margin-bottom: 12px;
    text-align: center;
    box-shadow: 0 3px 8px rgba(0,0,0,0.4);
  }
  .oss-header h1 {
    margin: 0;
    font-size: 28px;
    color: #fff;
    font-weight: 700;
    text-shadow: 0 3px 6px rgba(0,0,0,0.8);
  }
  .oss-header h4 {
    margin: 2px 0 0 0;
    color: #f0f0f0;
    font-style: italic;
    font-size: 14px;
    text-shadow: 0 2px 5px rgba(0,0,0,0.6);
  }

  /* OSS awareness line */
  .oss-quote-wrap { display:flex; justify-content:center; margin: 6px 0 16px 0; }
  .oss-quote {
    width: min(900px, 85vw);
    background: rgba(0,0,0,0.6);
    border-left: 4px solid #fff;
    padding: 6px 10px;
    font-style: italic;
    font-size: 15px;
    border-radius: 4px;
    color: #fff;
    font-weight: 600;
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
    background: rgba(255,255,255,0.85);
    border: 1.5px solid rgba(209,213,219,0.6);
    border-radius: 10px;
    padding: 12px 14px;
    transition: all 0.2s ease;
    box-shadow: 0 2px 6px rgba(0,0,0,0.2);
  }
  .card:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 14px rgba(0,0,0,0.3);
    background: rgba(255,255,255,0.95);
  }

  .title {
    margin: 0 0 4px 0;
    font-size: 18px;
    font-weight: 700;
    color: #000;
  }
  .tagline {
    margin: 0 0 8px 0;
    color: #1a1a1a;
    font-size: 14px;
    font-weight: 500;
    font-style: italic;
  }
  .pill {
    margin: 6px 0 10px 0;
    padding: 6px 8px;
    background: rgba(246,247,251,0.95);
    border: 1px solid #e4e7ef;
    border-radius: 6px;
    min-height: 32px;
    font-size: 13px;
    font-style: italic;
    color: #000;
    font-weight: 500;
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
    background: rgba(255,255,255,0.9);
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
    <!-- 1) ScanOSS -->
    <div class="card">
      <h3 class="title">ScanOSS</h3>
      <div class="tagline"><em>Best for: Code snippet &amp; copyright scanning</em></div>
      <div class="pill" id="scanoss-pill">📡 ScanOSS detects open-source components from code snippets.</div>
      <a class="open-btn" href="https://scanoss-scan.streamlit.app/" target="_blank">Open ScanOSS</a>
    </div>

    <!-- 2) ScanCode Toolkit -->
    <div class="card">
      <h3 class="title">ScanCode Toolkit</h3>
      <div class="tagline"><em>Best for: Licenses, copyrights &amp; SBOM export</em></div>
      <div class="pill" id="scancode-pill">📑 ScanCode detects licenses, copyrights, and dependencies.</div>
      <a class="open-btn" href="https://scancodetoolkit.streamlit.app/" target="_blank">Open ScanCode</a>
    </div>

    <!-- 3) FOSSology -->
    <div class="card">
      <h3 class="title">FOSSology</h3>
      <div class="tagline"><em>Best for: In-depth license compliance reports</em></div>
      <div class="pill" id="fossology-pill">🧩 FOSSology is an OSS license compliance toolkit.</div>
      <a class="open-btn" href="https://fosslogy.streamlit.app/" target="_blank">Open FOSSology</a>
    </div>

    <!-- 4) Syft -->
    <div class="card">
      <h3 class="title">Syft</h3>
      <div class="tagline"><em>Best for: SBOM generation &amp; license fetching</em></div>
      <div class="pill" id="syft-pill">🔍 Syft generates SBOMs (Software Bill of Materials).</div>
      <a class="open-btn" href="https://oss-compliance.streamlit.app/" target="_blank">Open Syft</a>
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
    height=740,
    scrolling=False,
)
